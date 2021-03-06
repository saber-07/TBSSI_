from tabnanny import verbose
from django.db import models
from django.urls import reverse
from apps.administration.models import CustomUser, Application, Filiale, Mesure, Departement
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
#les modeles utilisés

#classe Tableau de bord (principale)
class TB(models.Model):
    Intitule = models.CharField(max_length=200, blank=False, unique=True)
    Objectif = models.CharField(max_length=200, blank=False)
    validation_rapport = models.BooleanField(default=False)

    def __str__(self):
        return self.Intitule

    def get_absolute_url(self):
        return reverse("tbb_detail", kwargs={"pk": self.pk})
    

    
#classe Indicateur 
class Indicateur(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    PERIODICITE_CHOICES =( 
                    ('Annuelle', 'Annuelle'),
                    ('Mensuelle', 'Mensuelle'),
                    )

    TYPE_INDICATEUR_CHOICES = (  
        ('IPP', 'Indicateurs de performance de productivité'),
        ('IPQ', 'Indicateurs de performance de qualité'),
        ('IPC', 'Indicateurs de performance de capacité'),
        ('IPS', 'Indicateurs de performance stratégiques'),
    )

    TYPE_DONNEES_CHOICES = (  
        ('Mesure', 'Mesure'),
        ('Application', 'Application'),
        ('Filiale', 'Filiale'),
        ('Standard', 'Standard'),
    )

    TYPE_MiniGraphe_CHOICES = (
        ('Lineaire', 'Lineaire'),
        ('Barres', 'Barres'),
        ('Camembert', 'Camembert'),
        ('Beignet', 'Beignet'),
        ('Radar', 'Radar'),



    )

    Intitule_Indicateur = models.CharField(max_length=100, blank=False, unique=True)
    Objectif = models.CharField(max_length=100, blank=False)
    Domaine = models.CharField(max_length=100, blank=False)
    Type = models.CharField(max_length=50, choices=TYPE_INDICATEUR_CHOICES, blank=False)
    Methode_calcul = models.CharField(max_length=200, blank=False)
    Periodicite = models.CharField(max_length=100, choices=PERIODICITE_CHOICES)
    Source = models.CharField(max_length=100, blank=False)
    validation_chef_dep = models.BooleanField(default=False)
    validation_directeur = models.BooleanField(default=False)

    type_donnees = models.CharField(max_length=100, default='Standard', choices=TYPE_DONNEES_CHOICES, blank=False,verbose_name='Type Données')
    TypeMiniGraphe = models.CharField(max_length=100, default='Barres', choices=TYPE_MiniGraphe_CHOICES, blank=False,verbose_name='Type Mini Graphe')

    #cle etrangere -> Graphe + TB
    Id_Graphe = models.ForeignKey('Graphe', on_delete=models.CASCADE, blank=False, verbose_name='Graphe Bilan')
    Id_TB = models.ForeignKey(TB, on_delete=models.CASCADE, verbose_name='Tableau de bord')


    def __str__(self):
        return self.Intitule_Indicateur
    
    def get_absolute_url(self):
        return reverse("indicateur_detail", kwargs={"pk": self.pk})
    

#classe Graphe 
class Graphe(models.Model):
    
    GRAPHES_CHOICES = (
    ('Barres horizontales','Barres horizontales'),
    ('Barres Verticales','Barres Verticales'),
    ('Lineaire','Lineaire'),
    ('Camembert','Camembert'),
    ('Beignet','Beignet')
    ) 

    Type = models.CharField(max_length=50, choices=GRAPHES_CHOICES)

    def __str__(self):
        return self.Type 

#classe donnée
class Donnee(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    Date = models.DateField(blank=False)
    Valeur = models.IntegerField(blank=False)
    #cle etrangere indicateur
    Id_Indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Valeur)

    def get_absolute_url(self):
        return reverse("data_detail", kwargs={"pk": self.pk})

class DonneeApplication(Donnee):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

class DonneeFiliale(Donnee):
    filiale = models.ForeignKey(Filiale, on_delete=models.CASCADE)

class DonneeMesure(Donnee):
    mesure = models.ForeignKey(Mesure, on_delete=models.CASCADE)

#classe interpretation
class Interpretation(models.Model):

    Contenu = models.TextField(blank=False)
    Id_Indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)

    validation_chef_dep = models.BooleanField(default=False)
    validation_directeur = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("interpretation_detail", kwargs={"pk": self.pk})


@receiver(post_save, sender=Indicateur, weak=False)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_indicateur",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
    )

@receiver(post_save, sender=Indicateur, weak=False)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "delete_indicateur",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
    )

@receiver(post_save, sender=Donnee)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_donnee",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

@receiver(post_save, sender=Donnee)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "delete_donnee",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )
@receiver(post_save, sender=DonneeApplication)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_donneeapplication",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

@receiver(post_save, sender=DonneeApplication)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "delete_donneeapplication",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

@receiver(post_save, sender=DonneeFiliale)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_donneefiliale",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

@receiver(post_save, sender=DonneeFiliale)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "delete_donneefiliale",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

@receiver(post_save, sender=DonneeMesure)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "change_donneemesure",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

@receiver(post_save, sender=DonneeMesure)
def set_permission(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    assign_perm(
        "delete_donneemesure",  # The permission we want to assign.
        instance.user,  # The user object.
        instance  # The object we want to assign the permission to.
   )

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

@receiver(post_save, sender=Indicateur)
def notification(sender, instance, created, *args, **kargs):

    template = render_to_string('home/email_template.html', {'indicateur':instance.Intitule_Indicateur, 'inge':instance.user})
    #Send email 
    #indicateur doit d abord etre validé par le chef dep
    if not instance.validation_chef_dep:
        email = EmailMessage(
        'Nouvel indicateur a valider',
        template,
        settings.EMAIL_HOST_USER,
        [instance.user.departements.chef_dep.email, 
        ],
        )
        email.fail_silently=False
        email.send()
    #des qu'il est validé, une notification est envoyé au directeur
    elif not instance.validation_directeur:
        email = EmailMessage(
        'Nouvel Indicateur a valider',
        template,
        settings.EMAIL_HOST_USER,
        [instance.user.directions.directeur.email, 
        ],
        ) 
        email.fail_silently=False
        email.send()


post_save.connect(notification, sender=Indicateur)


#fonction envoi notif validation interpretation
@receiver(post_save, sender=Interpretation)
def notificationInter(sender, instance, created, *args, **kargs):

    template = render_to_string('home/email_templateInter.html', {'indicateur':instance.Id_Indicateur, 'inge':instance.Id_Indicateur.user})
    #Send email 
    #indicateur doit d abord etre validé par le chef dep
    if not instance.validation_chef_dep:
        email = EmailMessage(
        'Nouvelle interpretation a valider',
        template,
        settings.EMAIL_HOST_USER,
        [instance.Id_Indicateur.user.departements.chef_dep.email, 
        ],
        )
        email.fail_silently=False
        email.send()
    #des qu'il est validé, une notification est envoyé au directeur
    elif not instance.validation_directeur:
        email = EmailMessage(
        'Nouvelle interpretation a valider',
        template,
        settings.EMAIL_HOST_USER,
        [instance.Id_Indicateur.user.directions.directeur.email, 
        ],
        ) 
        email.fail_silently=False
        email.send()



post_save.connect(notificationInter, sender=Interpretation)