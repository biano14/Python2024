# lista 
cidades = ['Brasilia', 'Taguatinga', 'Planaltina', 'Ceilandia', 'Samanbaia', 'Riacho fundo', 'Candangolancia', 'Nucleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guara', 'Valparaiso', 'Novo gama', 'Céu azul', 'Lago Azul', 'Formosa', 'Estrutural', 'Águas claras', 'Arniqueiras', 'Areal', 'Sol nascente', 'Sol nascente', 'Dvo', 'São Sebastião', 'Dvo']

#usuario pesquisa pela cidade
cidade_pesquisada = input("Cidade a ser pesquisada: ").capitalize()

#pega o indice do item da pesquisa

#verifica se a cidade existe
try:
    indice = cidades.index(cidade_pesquisada)
    print(f'{cidade_pesquisada} encontrada no indice {indice}.')
except:
    print(f'Não foi possível encontrar {cidade_pesquisada}.')