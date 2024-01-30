class Restaurante:
    # encapsulando os atributos, alterações diretas objeto.atributo ficam indisponíveis
    restaurantes = list()
    _nome = ''
    _especialidade = ''
    _ativo = False


    def __init__(self, _nome, _especialidade):
        self._nome = _nome.title()
        self._especialidade = _especialidade.title()
        self._ativo = False
        Restaurante.restaurantes.append(self) 
      
    def __str__(self):
        return f'''
        Restaurante: {self._nome}
        _Especialidade: {self._especialidade} 
        _Ativo: {self._ativo}'''
    
    @classmethod # boa prática anotar métodos utilizados pela classe
    def listar_restaurantes(cls): # pedem parâmetro cls -//self
        lista = cls.restaurantes # cls.restaurantes // self.nome
        print(f'{'_Nome do Restaurante'.ljust(15)} | {'_Especialidade'.ljust(15)} | {'_Ativo'.ljust(15)}')

        for restaurante in lista:
            # ljust(int) aplica espaçamento
            print(f'_Nome: {restaurante._nome} | _Especialidade: {restaurante._especialidade} | Ativo: {restaurante._ativo}')             

    @property
    def ativo(self):
        return "_Ativo" if self._ativo == True else "Desativado"

    def ativar(self):
        self._ativo = not self._ativo # not inverte o False
        return self._ativo
     
# objeto com construtor
restaurante_italiano = Restaurante('Fastioli', 'Massas')
restaurante_italiano.ativar()
print(restaurante_italiano)



