from django.contrib import admin
from .models import Kategoriler,Markalar,Urunler,Etiketler

class KategorilerAdmin(admin.ModelAdmin):
    list_display = ['isim',"seo_title","slug","aktifmi"]
    list_filter = ["aktifmi"]
    search_fields = ["isim","seo_title","slug"]
    prepopulated_fields = {"slug": ("isim",)}

admin.site.register(Kategoriler, KategorilerAdmin)

class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim',"seo_title","slug","aktifmi","resim"] 
    list_filter = ["aktifmi"]
    search_fields = ["isim","seo_title","slug"]
    prepopulated_fields = {"slug": ("isim",)}

admin.site.register(Markalar, MarkalarAdmin)

class UrunlerAdmin(admin.ModelAdmin):
    list_display = ['isim','fiyat','marka','kategori','indirimli_fiyat','aktifmi','resim','tarih']
    list_filter = ['aktifmi','isim','kategori','marka']
    search_fields = ['isim','seo_title','slug']

admin.site.register(Urunler, UrunlerAdmin)
admin.site.register(Etiketler)