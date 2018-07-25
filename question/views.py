from django.shortcuts import HttpResponse, Http404, render, get_object_or_404
from question import views
from question.models import Question, QuestionReponse, User, Choix, Reponse
from question.forms import ChoixForm
from django.views.generic import TemplateView

def get_random():
    return Question.objects.order_by("?")[:3]


def question_du_jour(request):
    #form = ChoixForm()
    questionsDuJour = get_random();
    questionReponse = {}
    for q in questionsDuJour:
        questionReponse[q] = QuestionReponse.objects.filter(question=q)

    return render(
        request,
        'question/question_du_jour.html',
        context={'questionsDuJour':questionsDuJour, 'questionReponse':questionReponse},
    )

#def question_form(request):
    #form = QuestionForm(request.POST, instance=question)
    
    #return render(request, 'question/question_form.html', locals())
#def questions(request):
    #questions = Question.objects.all()
    #return render(request, 'question/questions.html', {'questions' : questions})


def index(request):
    #question = Question.objects.order_by('?').first()

    return render(request, 'index.html')