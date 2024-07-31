# Entrada de dados 
nome = input('Informe seu nome: ')

# Lista de cursos

print(f'{'='*30} LISTA DE CURSOS {'='*30}\n')
print('1 - Operador de Micro.')
print('2 - Desenvolvedor Java')
print('3 - Desenvolvedor Python.')
print('4 - Desenvolvedor Front-End.')
print('5 - Montador e reparador de Micro.')

# seleção de curso
opcao = input ('\nEscolha sua opção de curso: ')

# o switch...case do python
match int(opcao):
    case 1: 
        print(f'{nome} se matriculou no curso de Operador de Micro.')
    case 2: 
        print(f'{nome} se matriculou no curso de Desenvolvedor Java.')
    case 3: 
        print(f'{nome} se matriculou no curso de Desenvolvedor Python.')
    case 4: 
        print(f'{nome} se matriculou no curso de Desenvolvedor Front-End.')
    case 5: 
        print(f'{nome} se matriculou no curso de Montador e reparador de Micro.')
# default
    case _: 
        print('Opcão inválida')
