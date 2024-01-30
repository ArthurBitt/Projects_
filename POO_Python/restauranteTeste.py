from modules.restaurante import Restaurante # __inicia pycache__ bytecode do código

restaurante_arabe = Restaurante('Halabi', 'Esfihas')
restaurante_japones = Restaurante('Hanabi', 'Sushi')
restaurante_italiano = Restaurante('Fastioli', 'Massas')

def main():
    restaurante_arabe.ativar()
    Restaurante.listar_restaurantes()
    

    
if __name__ == '__main__':
    main()