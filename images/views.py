


from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm

# Create your views here.

# 🏠 Page d'accueil : liste des images
def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/image_list.html', {'images': images})

# 📜 Détail d'une image
def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'images/image_detail.html', {'image': image})

# 📤 Upload d'une image
def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'images/upload_image.html', {'form': form})

# ❌ Supprimer une image
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('image_list')
