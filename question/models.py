from django.db import models

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
    
    nom = models.CharField(max_length=100, verbose_name="Nom utilisateur")
    prenom = models.CharField(max_length=100, verbose_name="Prénom utilisateur")
    mail = models.CharField(max_length=100, verbose_name="Mail")
    age = models.IntegerField(verbose_name="Age")
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
