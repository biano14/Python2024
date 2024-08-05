#lista
cobras = ['Sucuri', 'Piton', 'Mamba Negra', 'Naja']

# exibe a lista original
for cobra in cobras:
    print (cobra)

# usuario informa o nome da nova cobra 
nova_cobra = input('\nInforme o nome da nova cobra: ')

#insere a nova cobra na lista
cobras.append(nova_cobra)

#exibe a nova lista
for cobra in cobras:
    print (cobra)

#ordena a lista
cobras.sort()

#exibe lsita ordenada
for cobra in cobras:
    print (cobra)