from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia


def getindexresponse(request):
# *getindexresponse Recebe uma requisição request e retorna um html com uma func response #
    query = Fotografia.objects.all()
    return render(request,'template_galeria/index.html', {"cards": query})

def imagem(request):
    return render(request, 'template_galeria/imagem.html')
# Create your views here