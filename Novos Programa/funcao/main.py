# função de boas vinda
def saudar(nome, idade):
    if idade >= 18:
        print(f'{nome}, seja bem vindo ao curso de Python!')
    else:
        print('Inscrição bloqueada, idade não pemitida')
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
#programa principal
saudar(nome, idade)
