from django import forms
from .models import Question, Reponse, QuestionReponse, User, Choix

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
'''
class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    #PasswordInput, RadioSelect et CheckboxInput qui existent
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
'''