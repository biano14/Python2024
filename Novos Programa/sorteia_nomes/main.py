import random

nomes = []

while True:
    print('1 - Inserir nome na lista.')
    print('2 - Sortear.')
    print('3 - Sair do programa.')
    
    opcao = input('Opção desejada: ')
    
    match opcao:
        case '1':
            nome = input('Insira o nome: ')
            nomes.append(nome)
            print(f'{nome} inserido com sucesso.')
            continue
        case '2':
            nome_sorteado = random.randint(0,len(nomes))
            print(f'Nome: {nomes[nome_sorteado - 1]}.')
            continue
        case '3':
            print('Progrma encerrado.')
            break
        case _:
            print('Opção inválida.')
            continue