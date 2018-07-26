from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import QuestionReponse, Choix, UserExtra

class ChoixForm(forms.ModelForm):

	class Meta:
		model = Choix
		fields = ['question_reponse']

	def __init__(self,*args,**kwargs):
		questionDuJour = kwargs.pop('questionDuJour')
		super(ChoixForm,self).__init__(*args,**kwargs)
		qr = QuestionReponse.objects.filter(question=questionDuJour)
		self.fields['question_reponse'] = forms.ModelChoiceField(queryset=qr, label=questionDuJour.texte)

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')	

class UserExtraForm(forms.ModelForm):
	
	class Meta:
		model = UserExtra
		fields = ['nom', 'prenom', 'mail', 'age', 'sexe', 'interesse_par', 'age_min_voulu', 'age_max_voulu']

