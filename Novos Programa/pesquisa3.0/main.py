# lista 
cidades = ['Brasilia', 'Taguatinga', 'Planaltina', 'Ceilandia', 'Samanbaia', 'Riacho fundo', 'Candangolancia', 'Nucleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guara', 'Valparaiso', 'Novo gama', 'Céu azul', 'Lago Azul', 'Formosa', 'Estrutural', 'Águas claras', 'Arniqueiras', 'Areal', 'Sol nascente', 'Sol nascente', 'Dvo', 'São Sebastião', 'Dvo']

#cidade a ser pesquisada
cidade_pesquisada = input('Cidade a ser pesquisada: ').capitalize()

#conta a quantidade de ocorrencias da palavra
cont = cidades.count(cidade_pesquisada)

#exibe
if cont == 1:
    print(f'{cidade_pesquisada} foi encontrada {cont} vez.')
elif cont == 0:
    print(f'{cidade_pesquisada} não foi encontrado')
else:
    print(f'{cidade_pesquisada} foi encontrada {cont} vezes.')    
