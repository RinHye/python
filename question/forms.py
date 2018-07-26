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
		self.fields['question_reponse'] = forms.ModelChoiceField(queryset=qr, label=questionDuJour.texte,)
		self.fields['question_reponse'].widget.attrs.update({
				'class': 'form-control form-control-sm'
			})

class UserForm(UserCreationForm):
    
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)

		for field in ['username', 'password1', 'password2']:
			self.fields[field].widget.attrs.update({
				'class': 'form-control form-control-sm'
			})

			

class UserExtraForm(forms.ModelForm):
	
	class Meta:
		model = UserExtra
		fields = ['nom', 'prenom', 'mail', 'age', 'sexe', 'interesse_par', 'age_min_voulu', 'age_max_voulu']
	
	def __init__(self, *args, **kwargs):
		super(UserExtraForm, self).__init__(*args, **kwargs)

		for field in ['nom', 'prenom', 'age', 'age_min_voulu', 'age_max_voulu']:
			self.fields[field].widget.attrs.update({
				'class': 'form-control form-control-sm'
			})
		
		for field in ['sexe', 'interesse_par']:
			self.fields[field].widget.attrs.update({
				'class': 'form-control form-control-sm'
			})

		self.fields['mail'].widget.attrs.update({
			'class': 'form-control form-control-sm'
		})

