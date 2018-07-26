from django.shortcuts import HttpResponse, Http404, render, redirect, get_object_or_404
from question import views
from question.models import Question, QuestionReponse, Choix, Reponse, QuestionDuJour, UserExtra
from question.forms import ChoixForm, UserForm, UserExtraForm
from datetime import date
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import request

def index(request):
    
    return render(request, 'index.html')

def inscription(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        extraform = UserExtraForm(request.POST)
        if all((userform.is_valid(), extraform.is_valid())) :
            user = userform.save()
            user.save()
            userextra = extraform.save(commit = False)
            userextra.user = user
            userextra.save()
            return redirect('index')
    else :
        userform = UserForm()
        extraform = UserExtraForm()

    return render(request, 'accounts/inscription.html', {'userform':userform, 'extraform':extraform})

def profile(request):
    extra = UserExtra.objects.get(user=request.user.username)
    print(request.user.username)
    userinfo = { 
        'user': request.user,
        'info' : extra
    }
    return render(request, 'accounts/profile.html', userinfo)

    

def get_random():
    return Question.objects.order_by("?").first()

def get_question_du_jour():
    q = QuestionDuJour.objects.filter(date=date.today()).first()
    if q is None:
        q = QuestionDuJour()
        q.question = get_random()
        q.save()
    return q.question

def question_du_jour(request):
    dejaRepondu = False
    questionDuJour = get_question_du_jour()
    user = User.objects.get(username=request.user.username)
    userExtra = UserExtra.objects.get(user=user)
    choixUser = Choix.objects.filter(user=userExtra)
    questionReponsesId = choixUser.values_list('question_reponse', flat=True)
    questionReponses = QuestionReponse.objects.filter(id__in=questionReponsesId)
    questionsId = questionReponses.values_list('question', flat=True)
    questions = Question.objects.filter(id__in=questionsId)
    for question in questions:
        if question.id == questionDuJour.id :
            dejaRepondu = True
    if request.method == "POST":
        form = ChoixForm(request.POST, questionDuJour=questionDuJour)
        if form.is_valid():
            choix = form.save(commit=False)
            choix.user = User.objects.get(username=request.user.username)
            choix.save()
            return redirect('matches')
    else:
        form = ChoixForm(questionDuJour=questionDuJour)

    return render(request, 'question/question_du_jour.html', {'questionDuJour':questionDuJour, 'dejaRepondu':dejaRepondu, 'form': form})

def matches(request):
    user = User.objects.get(username=request.user.username)
    userExtra = UserExtra.objects.get(user=user)

    """
    Match :
    - Récupérer user connecté
    - Tranche d'age recherchée
    - Interessé par
    - Choix
    - Récupérer les personnes qui tranche dage = tranche dage du connecté
    - Age correspondant tranche d'age
    - Récupérer les personnes qui intéressées par sexe du mec connecté et que mec connecté interessé par sexe de ces personnes
    - Choix des personnes identiques au mec connecté

    """
    match = UserExtra.objects.filter(Q(age_min_voulu__lte=userExtra.age) & \
                                     Q(age_max_voulu__gte=userExtra.age) & \
                                     Q(age__gte=userExtra.age_min_voulu) & \
                                     Q(age__lte=userExtra.age_max_voulu) &
                                     (Q(interesse_par=userExtra.sexe) | Q(interesse_par='T'))) \
                             .exclude(user=user)
    if (userExtra.interesse_par != 'T'):
        match.filter(sexe=userExtra.interesse_par)

    choixUser = Choix.objects.filter(user=userExtra)
    questionReponses = choixUser.values('question_reponse')
    choix = Choix.objects.select_related('user').filter(question_reponse__in=questionReponses).exclude(user=userExtra)
    matchChoix = choix.values_list('user', flat=True)
    users = UserExtra.objects.filter(pk__in=matchChoix)
    matchFinal = match.intersection(users)

    return render(request, 'question/matches.html', {'matchFinal':matchFinal})