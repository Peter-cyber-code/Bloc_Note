from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from notes.models import Login, Note 


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['titre', 'categorie', 'contenu', 'media']
        widgets = {
            'titre': forms.TextInput(attrs={'class':'form-control shadow-sm mb-3',
                                                    'placeholder':'Titre de la note'}),
            'categorie': forms.Select(attrs={
                                        'class':'form-select shadow-sm mb-3'}),
            'contenu': forms.Textarea(attrs={
                                            'class':'form-control shadow-sm mb-3',
                                            'placeholder': 'Contenu de la note',
                                            'rows': 5}),
            'media': forms.ClearableFileInput(attrs={
                                                        'class': 'form-control shadow-sm mb-3'
            }) ,                             
         }