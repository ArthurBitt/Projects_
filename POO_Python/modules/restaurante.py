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
        print(f'{'Nome do Restaurante'.ljust(15)} | {'Especialidade'.ljust(15)} | {'Ativo'.ljust(15)}')

        for restaurante in lista:
            # ljust(int) aplica espaçamento
            print(f'Nome: {restaurante._nome.ljust(15)} | Especialidade: {restaurante._especialidade.ljust(15)} | Ativo: {restaurante._ativo}')             

    @property
    def ativo(self):
        return "Ativo" if self._ativo == True else "Desativado"

    def ativar(self):
        self._ativo = not self._ativo # not inverte o False
        return self._ativo
     



