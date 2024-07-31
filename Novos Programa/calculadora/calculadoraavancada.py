import os
while True:
# entrada de dados
    x = float(input('Informe um número: ').replace(',','.'))
    y = float(input('Informe outro número: ').replace(',','.'))

    print(f'{'='*30} Calculadora {'='*30}\n')
    print('1 - Soma.')
    print('2 - Subtração.')
    print('3 - Divisão.')
    print('4 - Multiplicação.')
    print('5 - Resto da Divisão.')
    print('6 - Potenciação.')

    opcao = input ('\nEscolha a operção que deseja fazer: ')
    
    os.system('cls')

    match int(opcao):
        case 1: 
            resultado = x + y
            print (f'O resultado da sua soma é {resultado}.')
        case 2: 
            resultado = x - y
            print (f'O resultado da sua subtração é {resultado}.')
        case 3: 
            if y != 0:
                resultado = x / y
                print (f'O resultado da sua divisão é {resultado}.')
            else:
                print('Informe um divisor diferente de zero e tente novamente.')
        case 4: 
            resultado = x * y
            print (f'O resultado da sua é multiplicação {resultado}.')
        case 5: 
            if y != 0:
                resultado = x % y
                print (f'O resto da sua é divisão {resultado}.')
            else: 
                print('Informe um divisor diferente de zero e tente novamente.')
        case 6: 
            resultado = x ** y
            print (f'O resultado da sua é potência {resultado}.')
# default
        case _: 
            print('Opcão inválida')
    # exibe o resultado na tela   
    continuar = input('Deseja realizar outra operação? (s/n) ').lower()
    if continuar == 's' :
        os.system('cls')
        continue
    else:
        print('Programa finalizado')
        break
