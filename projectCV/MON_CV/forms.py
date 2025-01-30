from django import forms
from .models import Etudiant, Experience, Formation, Langue, Competence, Projet

# Formulaire pour le modèle Étudiant
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'tel', 'adresse', 'photo']

# Formulaire pour le modèle Expérience
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['poste', 'entreprise', 'date_debut', 'date_fin', 'description']

# Formulaire pour le modèle Formation
class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['diplome', 'etablissement', 'date_debut', 'date_fin']

# Formulaire pour le modèle Langue
class LangueForm(forms.ModelForm):
    class Meta:
        model = Langue
        fields = ['libelle', 'niveau']

# Formulaire pour le modèle Compétence
class CompetenceForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = ['libelle', 'niveau']

# Formulaire pour le modèle Projet
class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'date_debut', 'date_fin']
