from django import forms
from django.contrib.auth.forms import UserCreationForm
from notes.models import  Note 


'''class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d’utilisateur",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ex : Jean Dupont"
        })
    )

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )

    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Nom d’utilisateur",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Jean Dupont"
        })
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )



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
        