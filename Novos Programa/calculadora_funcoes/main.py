# funções
def mostrar_menu():
    print('1 - Somar.')
    print('2 - Subtrair')
    print('3 - Multiplicar.')
    print('4 - Dividir')
    print('5 - Extrair o resto da divisão.')
    print('6 - Potênciação.')
    print('7 - Sair do progrma')

somar       = lambda x,y: x + y
subtrair    = lambda x,y: x - y
multiplicar = lambda x,y: x * y
dividir     = lambda x,y: x / y
resto       = lambda x,y: x % y
potenciacao = lambda x,y: x ** y

#programa principal
if __name__ == '__main__':
    while True:
        mostrar_menu()
        try:
            opcao = input('Opção desejada: ')
            if opcao != '7':
                if opcao not in ('1','2','3','4','5','6'):
                    print('Opção invalida')
                else:
                    x = float(input("Informe o valor de x: ").replace(',','.'))    
                    y = float(input("Informe o valor de y: ").replace(',','.'))    
                    match opcao:
                        case '1':
                            print(f'O valor da soma entre {x} e {y} é {somar(x,y)}')
                            continue
                        case '2':
                            print(f'O valor da subtração entre {x} e {y} é {subtrair(x,y)}')
                            continue
                        case '3':
                            print(f'O valor da multiplicação entre {x} e {y} é {multiplicar(x,y)}')
                            continue
                        case '4':
                            print(f'O valor da divisão de {x} por {y} é {dividir(x,y)}')
                            continue
                        case '5':
                            print(f'O resto da divisão de {x} por {y} é {resto(x,y)}')
                            continue
                        case '6':
                            print(f'O valor de {x} elevado a {y} é {potenciacao(x,y)}')
                            continue
            else:
                print('Programa encerrado')
                break
        except:
            print('Impossível verificar opção.')
            break