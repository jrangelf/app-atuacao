from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),	
    path('entradadados/', views.entradadados, name='entradadados'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('consulta/', views.consulta, name='consulta'),      

]   