class Restaurante:
    # encapsulando os atributos, alterações diretas objeto.atributo ficam indisponíveis
    restaurantes = list()
    _nome = ''
    _especialidade = ''
    _ativo = False


    def __init__(self, _nome, _especialidade):
        self._nome = _nome.title()
        self._especialidade = _especialidade.title()
        self.__ativo = False
        Restaurante.restaurantes.append(self) 
      
    def __str__(self):
        return f'''
        Restaurante: {self._nome}
        _Especialidade:{self._especialidade} 
        _Ativo:{self._ativo}'''
    
    
    def listar_restaurantes():
        lista = Restaurante.restaurantes
        print(f'{'_Nome do Restaurante'.ljust(15)} | {'_Especialidade'.ljust(15)} | {'_Ativo'.ljust(15)}')

        for restaurante in lista:
            # ljust(int) aplica espaçamento
            print(f'_Nome: {restaurante._nome} | _Especialidade: {restaurante._especialidade} | _Ativo: {restaurante._ativo}')             

    @property
    def ativo(self):
        return "_Ativo" if self._ativo == True else "Desativado"
    
    @property
    def especialidade(self):
        return f"Categoria: { self._especialidade} "
        

# objeto com construtor
restaurante_italiano = Restaurante('Fastioli', 'Massas')

restaurante_italiano.nome = 'qualquer coisa' # protegendo o atributo não altera o valor diretamente
print(restaurante_italiano._nome) # resultado




