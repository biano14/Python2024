# lista de frutas
frutas = ['Maracujá', 'Maça', 'Laranja', 'Banana', 'Uva', 'Abacaxi']

# exibe a lista e os índices
for i in range(len(frutas)):
    print(f'Frutas de índice {i}: {frutas[i]}.')

# usuário informa o índice do item a ser separado
indice = int(input('Informe o índice do iem que deseja separar: '))

# separa o item
fruta = frutas.pop(indice)

# exibe o item separad
print(f'\n{fruta}\n')

for i in range(len(frutas)):
    print(f'Frutas de índice {i}: {frutas[i]}.')