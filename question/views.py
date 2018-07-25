from django.shortcuts import HttpResponse, Http404, render, redirect, get_object_or_404
from question import views
from question.models import Question, QuestionReponse, Choix, Reponse, QuestionDuJour, UserExtra
from question.forms import ChoixForm
from datetime import date
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db.models import Q

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
    questionDuJour = get_question_du_jour()
    print(request.POST)
    if request.method == "POST":
        form = ChoixForm(request.POST, questionDuJour=questionDuJour)
        if form.is_valid():
            choix = form.save(commit=False)
            choix.user = User.objects.get(username=request.user.username)
            choix.save()
            return redirect('matches')
    else:
        form = ChoixForm(questionDuJour=questionDuJour)

    return render(request, 'question/question_du_jour.html', {'questionDuJour':questionDuJour, 'form': form})

def index(request):

    return render(request, 'index.html')

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
                                     Q(age__lte=userExtra.age_max_voulu)) \
                             .exclude(user=user)
    print(match)
    return render(request, 'question/matches.html')