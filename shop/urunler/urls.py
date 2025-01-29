from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('basarisiliklarim/', views.basarisiliklarim, name='basarisiliklarim'),
    path('urun-detay/<slug>/', views.urun_detay, name='urun_detay'),
]
