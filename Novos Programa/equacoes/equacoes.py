import math

# Função menu
def mostrar_menu():
    print('\n')
    print('1 - Calcular equação do 1° grau.')
    print('2 - Calcular equação do 2° grau.')
    print('3 - Sair do programa.')
    print('\n')

# Equação do 2° grau
def calcular_grau_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x,
    else:
        return None,

def exibir_resultados(resultado, grau):
    if resultado is None:
        print('A equação não possui raízes reais.')
    elif grau == 1:
        print(f'Valor de x é {resultado}')
    elif grau == 2:
        if isinstance(resultado, tuple):
            x1, x2 = resultado
            print(f'Valor de x1 é {x1}.')
            print(f'Valor de x2 é {x2}.')
        else:
            print('A equação não possui raízes reais.')
# Equação do 1° grau
calcular_grau_1 = lambda a, b: -b / a 

def verifica_a(a):
    while True:
        try:
            valor = float(a)
            if valor == 0:
                print("O coeficiente não pode ser zero. Por favor, insira um valor diferente de zero.")
            else:
                return valor
        except:
            print("Entrada inválida. Por favor, insira um número válido.")