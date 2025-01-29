from django.shortcuts import render, get_object_or_404
from .models import Urunler

# Create your views here.

def index(request):
    urunler = Urunler.objects.filter(anasayfa=True)
    return render(request, "index.html", {"urunler":urunler})

def basarisiliklarim(request):
    return render(request, "basarisiliklarim.html")    

def urun_detay(request, slug):
    urun = get_object_or_404(Urunler, slug=slug)
    return render(request, "urun.html", {"urun":urun})