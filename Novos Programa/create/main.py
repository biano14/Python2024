#lista de nomes 
nomes = []

while True: 
    print('\n1 - Inserir novo nome.')
    print('2 - Exibir lista de nomes.')
    print('3 - Ordena lista.')
    print('4 - Sair do programa.\n')

    #opcao do usuario
    opcao = input('Opção do usuário: ')

    # verifica opcao escolhida
    match opcao:
        case '1':
            novo_nome = input('\nInsira o novo nome: ').capitalize()
            nomes.append(novo_nome)
            print(f'\n{novo_nome} inserido com sucesso.')
            continue
        case '2' :
            print(f'{10*'-'}LISTA DE NOMES{10*'-'}\n')
            for nome in nomes:
                print(f'{nome}\n')
            continue
        case '3':
            nomes.sort() 
            print(f'{10*'-'}LISTA DE NOMES{10*'-'}\n')
            for nome in nomes:
                print(f'{nome}\n')
            continue
        case '4':
            break
        case _:
            print('Opção Invalida')
            continue