#executando loop infinito
while True:
    #entrada de dados
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))

# verifica maioridade do usúario:
    if idade >= 18:
        print(f'{nome} é maior de idade.')
    else:
        print(f'{nome} é menor de idade.')

# verifica se o usuário deseja continuar    
    continuar = input('Deseja continuar? (s/n)').lower()
    if continuar == 's' :
        continue
    else:
        print('Programa finalizado')
        break