from django.contrib import admin
from .models import Question, Reponse, User, QuestionReponse, Choix
# Register your models here.

#Les tables modifiables et affichées coté admin
class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ('titre','texte')
    list_filter = ('titre', 'texte',)
    ordering = ('titre',)
    search_fields = ('titre', 'texte')
    
class QuestionReponseAdmin(admin.ModelAdmin):
    
    list_display = ('question','reponse')
    list_filter = ('question', 'reponse',)
    ordering = ('question',)
    search_fields = ('question', 'reponse')
    
class UserAdmin(admin.ModelAdmin):
    
    list_display = ('nom','prenom', 'mail', 'age')
    list_filter = ('nom', 'prenom',)
    ordering = ('nom',)
    search_fields = ('nom', 'prenom')
    
class ChoixAdmin(admin.ModelAdmin):
    
    list_display = ('question_reponse','user')
    list_filter = ('question_reponse', 'user',)
    ordering = ('user',)
    search_fields = ('user', 'question_reponse')
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse)
admin.site.register(QuestionReponse, QuestionReponseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Choix)
