"""
URL configuration for BANQUE_CV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MON_CV import views
from django.conf import settings
from django.conf.urls.static import static
from MON_CV.views import telecharger_cv_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Page d'accueil
    path('register/', views.register, name='register'),  # Inscription
    path('login/', views.login_user, name='login'),  # Connexion
    path('ajouter_cv/', views.ajouter_cv, name='ajouter_cv'),
    path('logout/', views.logout_user, name='logout'),  # Déconnexion
    path('etudiant/', views.etudiant_form, name='etudiant_form'),
    path('experience/', views.ajouter_experience, name='ajouter_experience'),
    path('formation/', views.ajouter_formation, name='ajouter_formation'),
    path('langue/', views.ajouter_langue, name='ajouter_langue'),
    path('competence/', views.ajouter_competence, name='ajouter_competence'),
    path('projet/', views.ajouter_projet, name='ajouter_projet'),
    path('selection-elements/', views.selection_elements, name='selection_elements'),
    path('generer_cv/', views.generer_cv, name='generer_cv'),
    path('sauvegarder_cv/', views.sauvegarder_cv, name='sauvegarder_cv'),
    path('mes_cvs/', views.mes_cvs, name='mes_cvs'),
    path('voir_cv/<int:cv_id>/', views.voir_cv, name='voir_cv'),
    path('cv/supprimer/<int:cv_id>/', views.supprimer_cv, name='supprimer_cv'),
    path('cv/<int:cv_id>/choisir_style/', views.choisir_style_cv, name='choisir_style_cv'),
    path('cv/<int:cv_id>/appercu/<str:style>/', views.appercu, name='appercu'),
    path('telecharger_cv/<int:cv_id>/<str:style>/', telecharger_cv_pdf, name='telecharger_cv'),
    # Autres URLs...
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

