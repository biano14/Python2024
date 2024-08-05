# lista de nomes
nomes = ['Fulano', 'Cicrano', 'Beltrano']

#usuário insere novo nome
novo_nome = input('Informe o novo nome: ').capitalize()
posicao = int(input('Informe a posição do novo nome: '))
posicao -= posicao
#insere o novo nome no local indicado
nomes.insert(posicao, novo_nome)
print('\n')
#imprime a lista
for nome in nomes:
    print (nome)

#ordena a lista
nomes.sort()
print('\n')
#imprime a lista ordena
for nome in nomes:
    print (nome)


