import math
# função menu
def mostrar_menu():
    print('1 - Calcular equação do 1° grau.')
    print('2 - Calcular equação do 2° grau.')
    print('3 - Sair do programa.')

#equação do 2° grau
def calcular_grau_2(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return 'A equação não possui raizes reais'
    elif delta == 0:
        return(-b)/(2*a)
    else:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
        yield x1
        yield x2


#equação do 1° grau
calcular_grau_1 = lambda a,b: -b/a

