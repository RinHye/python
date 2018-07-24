from django.db import models

# Create your models here.
class User(models.Model):
    
    nom = models.CharField(max_length=100, verbose_name="Nom utilisateur")
    prenom = models.CharField(max_length=100, verbose_name="Prénom utilisateur")
    mdp = models.CharField(max_length=24, verbose_name="Mot de passe")
    mail = models.CharField(max_length=100, verbose_name="Mail")
    age = models.IntegerField(verbose_name="Age")
    #photo = models.ImageField(upload_to='static/photos')
    
    #accéder à la liste des choix d'un user : user.choix_set.all()
    class Meta:
        verbose_name = "utilisateur"
    
    def __str__(self):
        return self.nom