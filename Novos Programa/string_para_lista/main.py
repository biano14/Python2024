''' variável
nome = 'John Connor'

# separa a string em uma lista
nome_completo = nome.split(' ')

# exibe a lista
for parte_nome in nome_completo:
    print(parte_nome, end=' ')# end é para eliminar a quebra de linha, substitui por espaço vazio'''

# usuário imforma o nome
nome = input('Informe o seu nome completo: ')

# separa as palavras do nome e capitula
nome_lista =  nome.split(' ')

# capitular as palavras do nome
for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize()
    
# junta o nome em uma variável
nome_completo = ' '.join(nome_lista)

# exibe na tela
print(nome_completo)