from django.contrib import admin
from .models import Eleve

# # Register your models here.
class EleveAdmin(admin.ModelAdmin):
     list_display ='firstname', 'lastname','password' # Champs à afficher dans la liste des élèves
    

admin.site.register(Eleve,EleveAdmin)

# @admin.register(Alumni)
# class AlumniAdmin(admin.ModelAdmin):
#     list_display = ('nom', 'prenom','ida')  # Champs à afficher dans la liste des anciens élèves
