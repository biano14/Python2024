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
                eq.exibir_resultados(resultado, 1)
                
            case '2':
                os.system('cls')
                a = eq.verifica_a(input('Valor de "a": ').replace(',', '.'))
                b = float(input('Valor de "b": ').replace(',', '.'))
                c = float(input('Valor de "c": ').replace(',', '.'))
                resultado = eq.calcular_grau_2(a, b, c) 
                eq.exibir_resultados(resultado, 2) 
            case '3':
                print('Programa encerrado.')
                break
