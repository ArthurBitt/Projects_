class Restaurante:
    restaurantes = list()
    nome = ''
    especialidade = ''
    ativo = False


    def __init__(self, nome, especialidade):
        self.nome = nome.title()
        self.especialidade = especialidade.title()
        self._ativo = False
        Restaurante.restaurantes.append(self) 
      
    def __str__(self):
        return f'''
        Restaurante: {self.nome}
        Especialidade:{self.especialidade} 
        Ativo:{self.ativo}'''
    
    
    def listar_restaurantes():
        lista = Restaurante.restaurantes
        print(f'{'Nome do Restaurante'.ljust(15)} | {'Especialidade'.ljust(15)} | {'Ativo'.ljust(15)}')

        for restaurante in lista:
            # ljust(int) aplica espaçamento
            print(f'Nome: {restaurante.nome} | Especialidade: {restaurante.especialidade} | Ativo: {restaurante.ativo}')             

    @property
    def ativo(self):
        return "Ativo" if self._ativo == True else "Desativado"

# objeto com construtor
restaurante_italiano = Restaurante('Fastioli', 'Massas')

Restaurante.listar_restaurantes() #ativo() interfere aqui
print(restaurante_italiano.ativo) # ativo() é chamado sem () por conta do @ property




