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
    delta = (b**2) - (4*a*c)
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f'Valor de x1 é {x1}.', f'Valor de x2 é {x2}.'
    elif delta == 0:
        x = -b / (2*a)
        return f'Valor de x é {x}'
    else:
        return 'A equação não possui raízes reais' 
    
# Equação do 1° grau
calcular_grau_1 = lambda a, b: -b / a  