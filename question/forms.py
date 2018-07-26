from django import forms
#from django.contrib.sessions import session
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

class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username','password1','password2') 

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)

		if commit:
			user.save()
		
		return user

class RegisterExtraForm(forms.ModelForm):
	
	class Meta:
		model = UserExtra
		fields = ('nom', 'prenom', 'mail', 'age', 'sexe', 'interesse_par', 'age_min_voulu', 'age_max_voulu')	

	def save(self, commit=True):
		extra = super(RegisterExtraForm, self).save(commit=False)
		extra.nom = self.cleaned_data['nom']
		extra.prenom = self.cleaned_data['prenom']
		extra.mail = self.cleaned_data['mail']
		extra.age = self.cleaned_data['age']
		extra.sexe = self.cleaned_data['sexe']
		extra.interesse_par = self.cleaned_data['interesse_par']
		extra.age_min_voulu = self.cleaned_data['age_min_voulu']
		extra.age_max_voulu = self.cleaned_data['age_max_voulu']
		
		if commit:
			extra.save()
	
		return extra
			
