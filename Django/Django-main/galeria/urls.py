from django.urls import path
from galeria.views import getindexresponse, imagem


urlpatterns = [
    path('',getindexresponse, name='index'),
    path('imagem/',imagem, name='imagem')
]



