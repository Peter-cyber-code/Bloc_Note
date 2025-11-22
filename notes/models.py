from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.username


class Note(models.Model):
    CATEGORIE_CHOICES = [
        ('Etudes', 'Etudes'),
        ('Projets', 'Projets'),
        ('Reunion', 'Réunion'),
        ('Autres', 'Autres')
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=120)
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES, default='Autres')
    contenu = models.TextField()
    media = models.FileField(
        upload_to='notes/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['pdf','docx','doc','mp4','mp3','jpg','png','jpeg'])]
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
