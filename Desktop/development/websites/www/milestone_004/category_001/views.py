from django.shortcuts import render
from .models import Category_001

# Create your views here.
def all_images(request):
    images = Category_001.objects.all()
    return render(request, "app_001/catagory_001.html", {"category_001": images})