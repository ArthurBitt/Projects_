class Restaurante:
    
    nome = ''
    especialidade = ''
    ativo = False

    # método construtor inicia o objeto 
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.ativo = False

# objeto com construtor
restaurante_italiano = Restaurante('Fastioli', 'Massas')
resutarantes = [restaurante_italiano]
# vars() exibe em formato de dicionário os atributos do objeto
print(vars(restaurante_italiano))
