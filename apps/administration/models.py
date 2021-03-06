from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

#les modeles utilisés

class Filiale(models.Model):

    nom_fil = models.CharField(max_length=60, null=True, blank=True)
    pdg = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom_fil

    def get_absolute_url(self):
        return reverse("filiale_detail", kwargs={"pk": self.pk})
    

class Direction(models.Model):

    nom_dir = models.CharField(max_length=60, null=True, blank=True)
    filiales = models.ForeignKey(Filiale, on_delete=models.CASCADE, null=True, blank=True)
    directeur = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom_dir
    
    def get_absolute_url(self):
        return reverse("direction_detail", kwargs={"pk": self.pk})
    

class Departement(models.Model):

    nom_dep = models.CharField(max_length=60, null=True, blank=True)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)
    chef_dep = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom_dep
    
    def get_absolute_url(self):
        return reverse("departement_detail", kwargs={"pk": self.pk})
    

class CustomUser(AbstractUser):

    POSTE_CHOICES=(
        ('PDG', 'PDG'),
        ('Directeur', 'Directeur'),
        ('Chef département', 'Chef département'),
        ('Ingénieur', 'Ingénieur')
    )

    SEXE_CHOICES=(
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin')
    )

    poste = models.CharField(max_length=50, choices=POSTE_CHOICES, null=True, blank=True)
    departements = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, blank=True)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)
    filiales = models.ForeignKey(Filiale, on_delete=models.CASCADE, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    sexe= models.CharField(max_length=10,choices=SEXE_CHOICES,default="Masculin")

    def get_absolute_url(self):
        return reverse("customuser_detail", kwargs={"pk": self.pk})
    

    def get_absolute_url(self):
        return reverse("customuser_detail", kwargs={"pk": self.pk})
    
class Application(models.Model):

    nom_app = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_app

    def get_absolute_url(self):
        return reverse("application_detail", kwargs={"pk": self.pk})
 
class Referentiel(models.Model):

    nom_referentiel = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_referentiel

    def get_absolute_url(self):
        return reverse("referentiel_detail", kwargs={"pk": self.pk})

class Domaine(models.Model):

    nom_domaine = models.CharField(max_length=20)
    referentiel = models.ForeignKey(Referentiel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_domaine

    def get_absolute_url(self):
        return reverse("domaine_detail", kwargs={"pk": self.pk})

class Categorie(models.Model):

    nom_categorie = models.CharField(max_length=20)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_categorie

    def get_absolute_url(self):
        return reverse("categorie_detail", kwargs={"pk": self.pk})
class Mesure(models.Model):

    nom_mesure = models.CharField(max_length=20)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_mesure

    def get_absolute_url(self):
        return reverse("mesure_detail", kwargs={"pk": self.pk})

@receiver(post_save, sender=CustomUser)
def user_post_save(sender, instance, created, *args, **kargs):

    if (instance.is_admin):
        group = Group.objects.get(name='Admin')  
        instance.groups.add(group)

    if(not instance.is_superuser):
        group = Group.objects.get(name=instance.poste) 
        instance.groups.add(group)
    

post_save.connect(user_post_save, sender=CustomUser)

@receiver(post_save, sender=CustomUser)
def directeur_affect(sender, instance, created, *args, **kargs):

    if (instance.poste == 'Directeur'):
        instance.directions.directeur = instance
        instance.directions.save()

@receiver(post_save, sender=CustomUser)
def departement_affect(sender, instance, created, *args, **kargs):

    if (instance.poste == 'Chef département'):
        instance.departements.chef_dep = instance
        instance.departements.save()

@receiver(post_save, sender=CustomUser)
def pdg_affect(sender, instance, created, *args, **kargs):

    if (instance.poste == 'PDG'):
        instance.filiales.pdg = instance
        instance.departements.save()

@receiver(pre_save, sender=CustomUser)
def username_affect(sender, instance, *args, **kargs):
    if(f"{instance.last_name}{instance.first_name}" != ""):
        instance.username = f"{instance.last_name}.{instance.first_name}"