from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from notes.forms import LoginUserForm, NotesForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from notes.models import Note
# Create your views here.


def home(request):
    return render(request, 'notes/home.html')


def ajouter_note(request):
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('liste-notes')
    else:
        form = NotesForm()
    return render(request, 'notes/ajouter_note.html', {'form': form})

from django.db.models import Q
def liste_notes(request):
    # ======= Recherche ==========

    notes = Note.objects.filter(user=request.user)
    query = request.GET.get('search')
    
    if query:
        notes = notes.filter(Q(titre__icontains=query) | Q(contenu__icontains=query))
        notes = notes.order_by('-date_creation')

    # ========== Filtrage ==============

    categorie = request.GET.get('categorie') # on récupère la catégorie envoyée 
    
    if categorie and categorie != "Autres":
        notes = notes.filter(categorie=categorie) 

    notes = notes.order_by('-date_creation')
    categories = [c[0] for c in Note.CATEGORIE_CHOICES] # on récupère la liste des catégories définies dans le modèle
        
    return render(request, 'notes/liste_notes.html', {'notes': notes, 'categories': categories, 'selected': categorie})

def voir_note(request, note_id):
    note = get_object_or_404(Note, user=request.user, id=note_id)
    return render(request, 'notes/voir_note.html', {'note': note})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginUserForm

def inscription(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("liste-notes")
    else:
        form = SignUpForm()

    return render(request, "notes/inscription.html", {"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect("liste-notes")

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("liste-notes")
        else:
            messages.error(request, "Nom d’utilisateur ou mot de passe incorrect.")
    else:
        form = LoginUserForm()

    return render(request, "notes/login_user.html", {"form": form})


    
def logout_user(request):
    logout(request)
    return redirect('login-user')


def update_note(request, note_id):
    note = get_object_or_404(Note, user=request.user, id=note_id)

    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('liste-notes')
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes/update_note.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, user=request.user, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('liste-notes')
    return render(request, 'notes/confirm_delete_note.html', {'note': note})
