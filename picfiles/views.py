from django.shortcuts import render
from . models import Image

def index(request):
    pics = Image.objects.all()
    return render(request, 'index.html', {'pics':pics})