import os
def mostrar_menu():
    print('1 - Calcular quadrilétero.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Calcular Trapezio.')
    print('5 - Sair do programa.')    
def calcular_quadrilatero(b):
    return b**2
def calcular_triangulo(b, h):
    return (b * h)/2
def calcular_circulo(r):
    return 3.14*r**2
def calcular_trapezio(b,bg,h):
    return ((b + bg) * h)/h    

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcao = input('Opção desejada: ')
        match opcao:
            case '1':
                try:
                    b = float(input('Informe o valor do lado do quadrado: ').replace(',','.'))
                    os.system('cls')
                    print(f'Área do quadrado: {calcular_quadrilatero(b)}')
                    print('\n')
                except Exception as e:
                    print(f'Não foi possivel calcular a área do quadrado')
                finally:        
                    continue
            case '2':
                try:
                    b = float(input('Informe o valor da base: ').replace(',','.'))
                    h = float(input('Informe o valor da altura: ').replace(',','.'))
                    os.system('cls')
                    print(f'Área do triângulo: {calcular_triangulo(b, h)}')
                    print('\n')
                except Exception as e:
                    print(f'Não foi possivel calcular a área do triângulo')
                finally:
                    continue
            case '3':
                try:
                    r = float(input('Informe o valor do raio: ').replace(',','.'))
                    os.system('cls')
                    print(f'Área da circunferência: {calcular_circulo(r)}.')
                    print('\n')
                except Exception as e:
                    print(f'Não foi possivel calcular a área do circulo')
                finally:
                    continue
            case '4':
                try:
                    b = float(input('Informe o valor da base menor: ').replace(',','.'))
                    bg = float(input('Informe o valor da base maior: ').replace(',','.'))
                    h = float(input('Informe o valor da altura: ').replace(',','.'))
                    os.system('cls')
                    print(f'Área do Trapézio: {calcular_trapezio(b,bg, h)}.')
                    print('\n')
                except:
                    print(f'Não foi possivel calcular a área do trapézio')
                finally:        
                    continue
            case '5':
                print('Programa encerrado.')
                break
            case _:
                print('Opção inválida.')