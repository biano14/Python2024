# lista 
cidades = ['Brasilia', 'Taguatinga', 'Planaltina', 'Ceilandia', 'Samanbaia', 'Riacho fundo', 'Candangolancia', 'Nucleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guara', 'Valparaiso', 'Novo gama', 'Céu azul', 'Lago Azul', 'Formosa', 'Estrutural', 'Águas claras', 'Arniqueiras', 'Areal', 'Sol nascente', 'Sol nascente', 'Dvo', 'São Sebastião', 'Dvo']

#usuario informa valor a ser pesquisado

cidade_pesquisa = input('Cidade a ser pesquisada: ').capitalize()

#verifica se a cidade existe

if cidade_pesquisa in cidades:
    print(f'Cidade {cidade_pesquisa} achada com sucesso.')
else:
    print('Não foi possivel encontrar a cidade')