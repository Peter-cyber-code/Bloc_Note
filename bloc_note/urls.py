
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from notes.views import ajouter_note, delete_note, home, inscription, liste_notes, login_user, logout_user, update_note, voir_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ajouter-note', ajouter_note, name='ajouter-note'),
    path('voir-note/<int:note_id>/', voir_note, name='voir-note'),
    path('update-note/<int:note_id>/', update_note, name='update-note'),
    path('delete-note/<int:note_id>/', delete_note, name='delete-note'),
    path('liste-notes', liste_notes, name='liste-notes'),
    path('logout-user', logout_user, name='logout-user'),
    path('login-user', login_user, name='login-user'),
    path('sign-user', inscription, name='sign-user'),
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

