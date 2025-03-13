from django.urls import path
from .views import image_list, image_detail, upload_image, delete_image

urlpatterns = [
    path('', image_list, name='image_list'),  # Page d'accueil : liste des images
    path('<int:image_id>/', image_detail, name='image_detail'),  # Détail d'une image
    path('upload/', upload_image, name='upload_image'),  # Upload d'une image
    path('<int:image_id>/delete/', delete_image, name='delete_image'),  # Suppression d'une image
]
