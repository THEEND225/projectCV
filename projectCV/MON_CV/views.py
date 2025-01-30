from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Etudiant
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import (
    EtudiantForm, ExperienceForm, FormationForm, LangueForm, CompetenceForm, ProjetForm
)
from .models import Etudiant
from django.shortcuts import render, redirect
from .models import Etudiant, Experience, Formation, Langue, Competence, Projet ,CV
from .forms import EtudiantForm, ExperienceForm, FormationForm, LangueForm, CompetenceForm, ProjetForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Etudiant  # Assurez-vous d'avoir l'accès à la base de données


def home(request):
    # Récupère tous les étudiants ayant rempli le formulaire
    etudiants = Etudiant.objects.all()
    return render(request, 'home.html', {'etudiants': etudiants})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def etudiant_form(request):
    try:
        etudiant = Etudiant.objects.get(user=request.user)
    except Etudiant.DoesNotExist:
        etudiant = None

    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            etudiant = form.save(commit=False)
            etudiant.user = request.user
            etudiant.save()
            return redirect('ajouter_cv')  # Redirige vers la page principale d'ajout de CV
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'ajouter_etudiant.html', {'form': form})


# Ajouter une expérience
@login_required
def ajouter_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.etudiant = request.user.etudiant
            experience.save()
            return redirect('ajouter_cv')
    else:
        form = ExperienceForm()

    return render(request, 'ajouter_experience.html', {'form': form})


# Ajouter une formation
@login_required
def ajouter_formation(request):
    if request.method == "POST":
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save(commit=False)
            formation.etudiant = request.user.etudiant
            formation.save()
            return redirect('ajouter_cv')
    else:
        form = FormationForm()

    return render(request, 'ajouter_formation.html', {'form': form})


# Ajouter une langue
@login_required
def ajouter_langue(request):
    if request.method == "POST":
        form = LangueForm(request.POST)
        if form.is_valid():
            langue = form.save(commit=False)
            langue.etudiant = request.user.etudiant
            langue.save()
            return redirect('ajouter_cv')
    else:
        form = LangueForm()

    return render(request, 'ajouter_langue.html', {'form': form})


# Ajouter une compétence
@login_required
def ajouter_competence(request):
    if request.method == "POST":
        form = CompetenceForm(request.POST)
        if form.is_valid():
            competence = form.save(commit=False)
            competence.etudiant = request.user.etudiant
            competence.save()
            return redirect('ajouter_cv')
    else:
        form = CompetenceForm()

    return render(request, 'ajouter_competence.html', {'form': form})


# Ajouter un projet
@login_required
def ajouter_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.etudiant = request.user.etudiant
            projet.save()
            return redirect('ajouter_cv')
    else:
        form = ProjetForm()

    return render(request, 'ajouter_projet.html', {'form': form})

def ajouter_cv(request):
    return render(request, 'ajouter_cv.html')

def selection_elements(request):
    # Récupérer l'étudiant connecté
    etudiant = Etudiant.objects.get(user=request.user)

    # Récupérer toutes les données associées à l'étudiant
    experiences = Experience.objects.filter(etudiant=etudiant)
    formations = Formation.objects.filter(etudiant=etudiant)
    langues = Langue.objects.filter(etudiant=etudiant)
    competences = Competence.objects.filter(etudiant=etudiant)
    projets = Projet.objects.filter(etudiant=etudiant)

    if request.method == 'POST':
        # Action pour supprimer tous les éléments sélectionnés
        action = request.POST.get('action')

        if action == 'remove_all':
            selected_experiences = request.POST.getlist('experiences')
            selected_formations = request.POST.getlist('formations')
            selected_langues = request.POST.getlist('langues')
            selected_competences = request.POST.getlist('competences')
            selected_projets = request.POST.getlist('projets')

            # Supprimer tous les éléments sélectionnés dans chaque catégorie
            if selected_experiences:
                Experience.objects.filter(id__in=selected_experiences).delete()
            if selected_formations:
                Formation.objects.filter(id__in=selected_formations).delete()
            if selected_langues:
                Langue.objects.filter(id__in=selected_langues).delete()
            if selected_competences:
                Competence.objects.filter(id__in=selected_competences).delete()
            if selected_projets:
                Projet.objects.filter(id__in=selected_projets).delete()

            # Retirer tous les éléments supprimés de la session
            request.session['selected_experiences'] = [
                exp_id for exp_id in request.session.get('selected_experiences', [])
                if exp_id not in selected_experiences
            ]
            request.session['selected_formations'] = [
                form_id for form_id in request.session.get('selected_formations', [])
                if form_id not in selected_formations
            ]
            request.session['selected_langues'] = [
                langue_id for langue_id in request.session.get('selected_langues', [])
                if langue_id not in selected_langues
            ]
            request.session['selected_competences'] = [
                competence_id for competence_id in request.session.get('selected_competences', [])
                if competence_id not in selected_competences
            ]
            request.session['selected_projets'] = [
                projet_id for projet_id in request.session.get('selected_projets', [])
                if projet_id not in selected_projets
            ]

        elif action == 'save':
            # Sauvegarder les éléments sélectionnés pour la construction du CV
            selected_experiences = request.POST.getlist('experiences')
            selected_formations = request.POST.getlist('formations')
            selected_langues = request.POST.getlist('langues')
            selected_competences = request.POST.getlist('competences')
            selected_projets = request.POST.getlist('projets')

            # Sauvegarder dans la session pour la génération du CV
            request.session['selected_experiences'] = selected_experiences
            request.session['selected_formations'] = selected_formations
            request.session['selected_langues'] = selected_langues
            request.session['selected_competences'] = selected_competences
            request.session['selected_projets'] = selected_projets

            return redirect('generer_cv')  # Rediriger vers la page de construction du CV

    return render(request, 'selection_elements.html', {
        'experiences': experiences,
        'formations': formations,
        'langues': langues,
        'competences': competences,
        'projets': projets,
    })


def generer_cv(request):
    # Récupérer l'étudiant connecté
    etudiant = Etudiant.objects.get(user=request.user)

    # Récupérer les éléments sélectionnés depuis la session
    selected_experiences = Experience.objects.filter(id__in=request.session.get('selected_experiences', []))
    selected_formations = Formation.objects.filter(id__in=request.session.get('selected_formations', []))
    selected_langues = Langue.objects.filter(id__in=request.session.get('selected_langues', []))
    selected_competences = Competence.objects.filter(id__in=request.session.get('selected_competences', []))
    selected_projets = Projet.objects.filter(id__in=request.session.get('selected_projets', []))

    return render(request, 'cv_style.html', {
            'etudiant': etudiant,
            'experiences': selected_experiences,
            'formations': selected_formations,
            'langues': selected_langues,
            'competences': selected_competences,
            'projets': selected_projets
        })


from datetime import date, datetime

def serialize_queryset(queryset):
    """Convertit les objets QuerySet en dictionnaire JSON sérialisable."""
    data = list(queryset.values())
    for item in data:
        for key, value in item.items():
            if isinstance(value, (date, datetime)):
                item[key] = value.isoformat()  # Convertit en format 'YYYY-MM-DD' ou 'YYYY-MM-DDTHH:MM:SS'
    return data

@login_required
def sauvegarder_cv(request):
    if request.method == "POST":
        nom_cv = request.POST.get('nom')
        if nom_cv:
            # Sérialiser les données en JSON tout en gérant les dates
            contenu = {
                'experiences': serialize_queryset(Experience.objects.filter(id__in=request.session.get('selected_experiences', []))),
                'formations': serialize_queryset(Formation.objects.filter(id__in=request.session.get('selected_formations', []))),
                'langues': serialize_queryset(Langue.objects.filter(id__in=request.session.get('selected_langues', []))),
                'competences': serialize_queryset(Competence.objects.filter(id__in=request.session.get('selected_competences', []))),
                'projets': serialize_queryset(Projet.objects.filter(id__in=request.session.get('selected_projets', []))),
            }

            # Sauvegarder le CV dans la base de données
            CV.objects.create(
                nom=nom_cv,
                etudiant=request.user.etudiant,
                contenu=contenu
            )
            messages.success(request, "Votre CV a été sauvegardé avec succès.")
            return redirect('home')  # Redirection vers le trombinoscope
        else:
            messages.error(request, "Veuillez entrer un nom pour le CV.")
    return render(request, 'sauvegarder_cv.html')


@login_required
def mes_cvs(request):
    # Vérifiez si l'utilisateur est connecté
    if request.user.is_authenticated:
        # Récupérer l'étudiant associé à l'utilisateur connecté
        etudiant = Etudiant.objects.get(user=request.user)
        # Filtrer les CVs associés à cet étudiant
        cvs = CV.objects.filter(etudiant=etudiant)
        return render(request, 'mes_cvs.html', {'cvs': cvs})
    else:
        return redirect('login')

@login_required
def voir_cv(request, cv_id):
    # Récupérer le CV par son ID
    cv = get_object_or_404(CV, id=cv_id, etudiant__user=request.user)
    return render(request, 'voir_cv.html', {'cv': cv})


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import CV
from django.contrib.auth.decorators import login_required

@login_required
def supprimer_cv(request, cv_id):
    # Vérifiez si le CV appartient à l'utilisateur connecté
    cv = get_object_or_404(CV, id=cv_id, etudiant__user=request.user)

    if request.method == 'POST':
        cv.delete()  # Supprimer le CV de la base de données
        messages.success(request, "Votre CV a été supprimé avec succès.")
        return redirect('mes_cvs')  # Rediriger vers la page des CVs

    return redirect('home')  # Rediriger vers la page d'accueil si la méthode n'est pas POST

from django.shortcuts import render, get_object_or_404
from .models import CV
from django.contrib.auth.decorators import login_required

@login_required
def choisir_style_cv(request, cv_id):
    # Vérifiez si le CV appartient à l'utilisateur connecté
    cv = get_object_or_404(CV, id=cv_id, etudiant__user=request.user)
    return render(request, 'choisir_style_cv.html', {'cv_id': cv_id})


@login_required
def appercu(request, cv_id, style):
    # Récupérer le CV par son ID
    cv = get_object_or_404(CV, id=cv_id, etudiant__user=request.user)

    # Passer les informations au template selon le style
    if style == 'style1':
        return render(request, 'cv_style1.html', {'cv': cv})
    elif style == 'style2':
        return render(request, 'cv_style2.html', {'cv': cv})
    elif style == 'style3':
        return render(request, 'cv_style3.html', {'cv': cv})
    elif style == 'style4':
        return render(request, 'cv_style4.html', {'cv': cv})
    else:
        return HttpResponse("Style non trouvé", status=404)

from weasyprint import HTML, CSS
from django.conf import settings
from django.templatetags.static import static
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

def telecharger_cv_pdf(request, cv_id, style):
    # Récupérer les données du CV
    cv = get_object_or_404(CV, id=cv_id)

    # Déterminer le template selon le style
    if style == 'style1':
        template_name = 'cv_style1.html'
    elif style == 'style2':
        template_name = 'cv_style2.html'
    elif style == 'style3':
        template_name = 'cv_style3.html'
    else:
        template_name = 'cv_style_default.html'

    # Générer le contenu HTML du CV
    html_content = render_to_string(template_name, {'cv': cv})

    # Ajouter le gestionnaire pour les fichiers statiques et médias
    def url_fetcher(url):
        if url.startswith(settings.STATIC_URL):
            path = url.replace(settings.STATIC_URL, settings.STATIC_ROOT)
        elif url.startswith(settings.MEDIA_URL):
            path = url.replace(settings.MEDIA_URL, settings.MEDIA_ROOT)
        else:
            raise ValueError(f"URL inconnue : {url}")
        return {'file_obj': open(path, 'rb')}

    # Générer le PDF
    pdf_buffer = BytesIO()
    HTML(string=html_content, base_url=request.build_absolute_uri('/')).write_pdf(target=pdf_buffer, url_fetcher=url_fetcher)
    pdf_buffer.seek(0)

    # Retourner le PDF comme réponse HTTP
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cv.nom}.pdf"'
    return response
