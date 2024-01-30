class Restaurante:
    
    nome = ''
    especialidade = ''
    ativo = False


    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.ativo = False

    # dunder methods - metodo str exibe o objeto formatado
    def __str__(self):
        return f'''
        Restaurante: {self.nome}
        Especialidade:{self.especialidade} 
        Ativo:{self.ativo}'''

# objeto com construtor
restaurante_italiano = Restaurante('Fastioli', 'Massas')
resutarantes = [restaurante_italiano]
print(restaurante_italiano)