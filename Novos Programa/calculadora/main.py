while True:
# entrada de dados
    x = int(input('Informe um número: '))
    y = int(input('Informe outro número: '))

    print(f'{'='*30} Calculadora {'='*30}\n')
    print('1 - Soma.')
    print('2 - Subtração.')
    print('3 - Divisão.')
    print('4 - Multiplicação.')

    opcao = input ('\nEscolha a operção que deseja fazer: ')

    match int(opcao):
        case 1: 
            resultado = x + y
        case 2: 
            resultado = x - y
        case 3: 
            resultado = x / y
        case 4: 
            resultado = x * y
# default
        case _: 
            print('Opcão inválida')
    # exibe o resultado na tela
    print (f'O resultado da sua é {resultado}.')
    continuar = input('Deseja continuar? (s/n)').lower()
    if continuar == 's' :
        continue
    else:
        print('Programa finalizado')
        break

