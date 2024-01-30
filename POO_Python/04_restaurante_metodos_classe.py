class Restaurante:
    restaurantes = list()
    nome = ''
    especialidade = ''
    ativo = False


    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.ativo = False
        Restaurante.restaurantes.append(self) 
        # não usa self.restaurante note que o self se refere ao próprio objeto. A lista sera referenciada
        # pela própria classe para conter todos os objetos restaurantes
    
    def __str__(self):
        return f'''
        Restaurante: {self.nome}
        Especialidade:{self.especialidade} 
        Ativo:{self.ativo}'''
    
    @classmethod
    def listar_restaurantes():
        lista = Restaurante.restaurantes
        for restaurante in lista:
            print(f'Nome: {restaurante.nome}|Especialidade: {restaurante.especialidade}|Ativo: {restaurante.ativo}')             

# objeto com construtor
restaurante_italiano = Restaurante('Fastioli', 'Massas')

Restaurante.listar_restaurantes()




