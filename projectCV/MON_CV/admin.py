from django.contrib import admin
from .models import Etudiant, Experience, Formation, Langue, Competence, Projet

# Modèle Etudiant
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'tel', 'adresse', 'photo')
    search_fields = ('prenom', 'nom', 'email')

# Modèle Experience
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('poste', 'entreprise', 'date_debut', 'date_fin', 'etudiant')
    search_fields = ('poste', 'entreprise', 'etudiant__prenom', 'etudiant__nom')

# Modèle Formation
class FormationAdmin(admin.ModelAdmin):
    list_display = ('diplome', 'etablissement', 'date_debut', 'date_fin', 'etudiant')
    search_fields = ('diplome', 'etablissement', 'etudiant__prenom', 'etudiant__nom')

# Modèle Langue
class LangueAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'niveau', 'etudiant')
    search_fields = ('libelle', 'etudiant__prenom', 'etudiant__nom')

# Modèle Competence
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'niveau', 'etudiant')
    search_fields = ('libelle', 'etudiant__prenom', 'etudiant__nom')

# Modèle Projet
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin', 'etudiant')
    search_fields = ('titre', 'etudiant__prenom', 'etudiant__nom')

# Enregistrement des modèles dans l'administration Django
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Langue, LangueAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Projet, ProjetAdmin)
