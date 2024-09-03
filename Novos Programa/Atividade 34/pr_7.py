# Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser)
# e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.
nomes = []

while True:
    print('\n1 - Inserir novo nome.')
    print('2 - Terminar cadastro e Exibir lista.\n')

    #opcao do usuario
    opcao = input('Opção do usuário: ')

    # verifica opcao escolhida
    match opcao:
        case '1':
            novo_nome = input('\nInsira o novo nome: ').capitalize()
            nomes.append(novo_nome)
            print(f'\n{novo_nome} inserido com sucesso.')
            continue
        case '2':
            nomes.sort()
            print(f'{10*'-'}LISTA DE NOMES{10*'-'}\n')
            for nome in nomes:
                print(f'{nome}\n')
            print(f"Quantidade de nome digitados {len(nomes)}")
            break
        case _:
            print('Opção Invalida')
            continue
