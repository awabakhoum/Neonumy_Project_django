from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from images.views import image_list  # Assure-toi d'importer la vue image_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', include('images.urls')),  # Inclure les URLs de l'application images
    path('', image_list, name='image_list'),  # Ajoute cette ligne pour la route racine
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
