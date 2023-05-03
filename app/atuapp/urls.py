from django.contrib import admin
from django.urls import path, include
from core import views

admin.site.site_header = 'ATUAÇÃO Web - Painel de Administração'
admin.site.site_title = 'Painel'

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include ('core.urls')),
]