def main():
    
    i = False
    x = float(input("Escolha o primeiro número: "))
    y = float(input("Escolha o segundo número: "))
    
    while i == False:
        operacao = int(input('''
          
            Qual a operação: 

        Multiplicação [1]
        Divisão       [2]
        subtração     [3]
        Soma          [4]
        Turn off      [5]
'''))
        if operacao == 1:

            print(f'{x} * {y} = {x * y}')
        elif operacao == 2:
            print(f'{x} / {y} = {x / y}')

        elif operacao == 3:
            print(f'{x} - {y} = {x - y}')

        elif operacao == 4:
            print(f'{x} + {y} = {x + y}')

        elif operacao == 5:
            print("Desligando...")
            i = True
            break;

        else:
            print("Operação iválida")
            continue;
        
        resp = input("Deseja continuar: S/N ")

        if resp.lower() == "n":
            i = True
            break;
        else:
            continue;
        
    

main()