# Lista
nomes = ['Fulano', 'Cicrano', 'Beltrano', 'João', 'Maria', 'José']

# exibe a lista e seus respectivos indices

for i in range(len(nomes)):
    print (f'Índice {i}: {nomes[i]}.')

    #quebra de linha
print('\n')

try:
    # usuario informa o indice
    indice = int(input('Informe o número do indice: '))

    # faz a alteração
    nomes[indice] = input('Informe o novo nome: ').capitalize()
except:
    print('Não foi possível fazer a alteração')

#exibe a nova lista

for i in range(len(nomes)):
    print(f'Indice {i}: {nomes[i]}.')