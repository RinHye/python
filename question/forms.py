from django import forms
from .models import Question, Reponse, QuestionReponse, User, Choix

class ChoixForm(forms.ModelForm):

    class Meta:
        model = Choix
        fields = ('question_reponse',)
'''
class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    #PasswordInput, RadioSelect et CheckboxInput qui existent
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
'''