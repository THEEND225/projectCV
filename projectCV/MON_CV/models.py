from django.db import models
from django.contrib.auth.models import User

# Modèle Étudiant
class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relation avec l'utilisateur Django
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Unicité pour éviter les doublons
    tel = models.CharField(max_length=15)
    adresse = models.TextField()
    photo = models.ImageField(upload_to='photos/', default='photos/default.jpg')

    def __str__(self):
        return f"{self.prenom} {self.nom}"


# Modèle Expérience professionnelle
class Experience(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="experiences")  # Relation avec l'étudiant
    poste = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.poste} chez {self.entreprise}"


# Modèle Formation académique
class Formation(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="formations")  # Relation avec l'étudiant
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.diplome} - {self.etablissement}"


# Choix pour les niveaux de compétence et de langue
NIVEAU_CHOICES = [
    ('Débutant', 'Débutant'),
    ('Intermédiaire', 'Intermédiaire'),
    ('Avancé', 'Avancé'),
    ('Expert', 'Expert'),
]

# Modèle Langue
class Langue(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="langues")  # Relation avec l'étudiant
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50, choices=NIVEAU_CHOICES)

    def __str__(self):
        return f"{self.libelle} ({self.niveau})"


# Modèle Compétence
class Competence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="competences")  # Relation avec l'étudiant
    libelle = models.CharField(max_length=100)
    niveau = models.CharField(max_length=50, choices=NIVEAU_CHOICES)

    def __str__(self):
        return f"{self.libelle} ({self.niveau})"


# Modèle Projet
class Projet(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="projets")  # Relation avec l'étudiant
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titre
class CV(models.Model):
    nom = models.CharField(max_length=255)  # Nom du CV
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)  # Lien avec l'étudiant
    date_creation = models.DateTimeField(auto_now_add=True)  # Date d'enregistrement
    contenu = models.JSONField()  # Contenu du CV (expériences, formations, etc.)

    def __str__(self):
        return self.nom