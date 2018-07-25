from django import forms
from .models import QuestionReponse, Choix

class ChoixForm(forms.ModelForm):

	class Meta:
		model = Choix
		fields = ['question_reponse']

	def __init__(self,*args,**kwargs):
		questionDuJour = kwargs.pop('questionDuJour')
		super(ChoixForm,self).__init__(*args,**kwargs)
		qr = QuestionReponse.objects.filter(question=questionDuJour)
		self.fields['question_reponse'] = forms.ModelChoiceField(queryset=qr, label=questionDuJour.texte)
