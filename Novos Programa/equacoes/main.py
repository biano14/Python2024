import equacoes as eq
import os

if __name__ == '__main__':
    while True:
        eq.mostrar_menu()
        opcoes = input('Opção escolhida: ')
        match opcoes:
            case '1':
                os.system('cls')
                a = float(input('Valor de "a": ').replace(',', '.'))
                b = float(input('Valor de "b": ').replace(',', '.'))
                resultado = eq.calcular_grau_1(a, b)
                print(f'Valor de x: {resultado}')
                
            case '2':
                os.system('cls')
                a = float(input('Valor de "a": ').replace(',', '.'))
                b = float(input('Valor de "b": ').replace(',', '.'))
                c = float(input('Valor de "c": ').replace(',', '.'))
                resultado = eq.calcular_grau_2(a, b, c)
                if isinstance(resultado, tuple):
                    for r in resultado:
                        print(r)
                else:
                    print(resultado)
                
            case '3':
                print('Programa encerrado.')
                break
