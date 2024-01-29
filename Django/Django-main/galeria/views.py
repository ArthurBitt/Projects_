from django.shortcuts import render
from django.http import HttpResponse

def getindexresponse(request):
# *getindexresponse Recebe uma requisição request e retorna um html com uma func response #
    return render(request, 'template_galeria\index.html')
def imagem(request):
    return render(request, 'template_galeria\imagem.html')
# Create your views here.
