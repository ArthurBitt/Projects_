def welcome (message) :
    print("*"*30)
    print(f'{message: ^30}')
    print("*"*30)

def main():
    

    i = False

    while  i == False :
        welcome("lalalalalalalalalal")
        x = int(input('digite um número e verifique se é par: '))
        if x % 2 == 0:
            print(f'{x} é par')
        else:
            print(f'{x} é ímpar')

        resp = str(input("Voce deseja consultar outro número: S/N "))

        if resp.lower() == "n":
            print("Saindo...")
            i = True
            break;

        else:
            continue;

main()