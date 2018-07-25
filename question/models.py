from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

#Toutes les tables de la BD
class Question(models.Model):
    
    titre = models.CharField(max_length=24, verbose_name="Titre de la question")
    texte = models.TextField(null=True, verbose_name="Question")
    #oneToOneField si relation 1-1
    class Meta:
        verbose_name = "Question"
        ordering = ['titre']
    
    def __str__(self):
        return self.titre

class Reponse(models.Model):
    
    reponse = models.TextField(null=True, verbose_name="réponse")

    class Meta:
        verbose_name = "Réponse"
    
    def __str__(self):
        return self.reponse

class QuestionReponse(models.Model):

    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)
    reponse = models.ForeignKey('Reponse', on_delete=models.CASCADE, null=False)
    class Meta:
        verbose_name = "question et réponse"
        ordering = ['question']
    
    def __Question__(self):
        return self.question
 
class User(models.Model):
    SEXES = (
        ('F', 'Femme'),
        ('M', 'Homme'),
        ('A','Ambigu')
    )
    INTERESSE = (
        ('F', 'Femme'),
        ('M', 'Homme'),
        ('T','Tout')
    )
    nom = models.CharField(max_length=100, verbose_name="Nom utilisateur")
    prenom = models.CharField(max_length=100, verbose_name="Prénom utilisateur")
    mail = models.CharField(max_length=100, verbose_name="Mail")
    age = models.IntegerField(verbose_name="Age", validators=[MaxValueValidator(100), MinValueValidator(15)])
    sexe = models.CharField(max_length=5, verbose_name="Sexe", choices=SEXES)
    interesse_par = models.CharField(max_length=5, verbose_name="Interessé par ", choices=INTERESSE)
    tranche_age = models.IntegerField(verbose_name="Tranche d'âge")
    #photo = models.ImageField(upload_to='static/photos')
    
    #accéder à la liste des choix d'un user : user.choix_set.all()
    class Meta:
        verbose_name = "utilisateur"
    
    def __str__(self):
        return self.nom

class Choix(models.Model):
    
    question_reponse = models.ForeignKey('QuestionReponse', on_delete=models.CASCADE, null=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    #en requete possibilite de faire : c.user.nom
    #oneToOneField si  relation 1-1
    class Meta:
        verbose_name = "choix"
        ordering = ['user']
    
    def __QuestionReponse__(self):
        return self.question_reponse
