class Restaurante:
    nome = ''
    especialidade = ''
    ativo = False


# objeto python 
restaurante_italiano = Restaurante()
restaurante_arabe = Restaurante()

restaurante_arabe.nome = 'Halabi'
restaurante_arabe.especialidade = 'Esfihas'
restaurante_arabe.ativo


restaurante_italiano.nome = 'Fastioli'
restaurante_italiano.especialidade = 'Massas'
restaurante_italiano.ativo = True


restaurante = [ restaurante_italiano,restaurante_arabe]

# print(restaurante_italiano)
##* dir() traz as informações do objeto
# print(dir(restaurante_italiano))

