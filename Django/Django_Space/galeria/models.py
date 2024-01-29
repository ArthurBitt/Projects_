from django.db import models

# Create your models here.

class Fotografia(models.Model):
    nome = models.CharField(max_length = 100, null = False,blank = False )
    legenda = models.CharField(max_length = 150, null = False,blank = False )
    descricacao = models.TextField(null = False,blank = False )
    fotoPath = models.CharField(max_length = 100, null = False,blank = False )

def __str__(self):
    return f"Fotografia [nome = {self.nome}]"

# ainda não esta sendo acessado, vzualização da page feita por dicionário