from django.shortcuts import render
from django.http import HttpResponse



def getindexresponse(request):
# *getindexresponse Recebe uma requisição request e retorna um html com uma func response #
    
    dados = {
        1:{"Nome": "Nebulosa de Carina",
        "Legenda": "webbtelescope.org/ NASA / James Webb"},
        2:{"Nome": "Galáxia NGC 1079",
        "Legenda": "nasa.org/ NASA / Hubble"}
    }


    return render(request, 'template_galeria\index.html', {"cards": dados})
def imagem(request):
    return render(request, 'template_galeria\imagem.html')
# Create your views here.
