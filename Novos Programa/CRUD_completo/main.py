import os

# Definindo as chaves
chaves = ('Nome Completo', 'Data de Nascimento', 'CPF', 'Telefone', 'Profissão', 'E-mail', 'Endereço')

# Lista inicial de usuários
usuarios = []

while True:
    print(f'\n{"-"*10} Banco de Usuários {"-"*10}')
    print('1 - Lista todos os usuários.')
    print('2 - Cadastra novo usuário.')
    print('3 - Pesquisa nome cadastrado.')
    print('4 - Alterar usuário cadastrado.')
    print('5 - Excluir usuário cadastrado.')
    print('6 - Sair do programa.')
    opcao = input('Opção Desejada: ')
    
    match opcao:
        case '1':
            print(f'\n{"="*10} LISTA DE USUÁRIOS {"="*10}\n')
            for usuario in usuarios:
                for chave in chaves:
                    if chave in usuario:
                        print(f'{chave}: {usuario[chave]}')
                print(f'\n{"-"*10}\n')
        case '2':
            usuario = {}
            for chave in chaves:
                usuario[chave] = input(f'Informe o/a {chave}: ')
            usuarios.append(usuario)
            print('\nUsuário cadastrado com sucesso!')
        case '3':
            print('Selecione o que deseja procurar')
            print('1 - Nome completo')
            print('2 - Data de Nascimento')
            print('3 - CPF')
            print('4 - Telefone')
            escolha = input('Informe o tipo de informação que deseja procurar: ')
            
            if escolha not in ['1', '2', '3', '4']:
                print('Escolha inválida!')
                continue
            
            chave_procurada = chaves[int(escolha) - 1]
            informacao = input(f'Digite o/a {chave_procurada} que deseja pesquisar: ')
            
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
            
            contador = 0
            for usuario in usuarios:
                if chave_procurada in usuario and usuario[chave_procurada] == informacao:
                    contador += 1

            print(f'{informacao} foi encontrado {contador} vezes.')
        case '4':
            for i, usuario in enumerate(usuarios):
                print(f'{i + 1}° usuário: {usuario}')
            try:
                indice = int(input('Informe o índice do usuário a ser alterado: ')) - 1
                if 0 <= indice < len(usuarios):
                    print("1 - Nome Completo")
                    print("2 - Data de Nascimento")
                    print("3 - CPF")
                    print("4 - Telefone")
                    print("5 - Profissão")
                    print("6 - E-mail")
                    print("7 - Endereço")
                    chave = int(input("Informe o número correspondente à chave que deseja alterar: ")) - 1
                    if 0 <= chave < len(chaves):
                        novo_valor = input(f'Informe o novo valor do campo {chaves[chave]}: ')
                        usuarios[indice][chaves[chave]] = novo_valor
                        print("Usuário alterado com sucesso.")
                    else:
                        print("Chave inválida!")
                else:
                    print("Índice de usuário inválido!")
            except ValueError:
                print('Entrada inválida! Informe números corretamente.')
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
        case '5':
            for i, usuario in enumerate(usuarios):
                print(f'{i + 1}° usuário: {usuario}')
            try:
                indice = int(input('Informe o índice do usuário que deseja deletar da lista: ')) - 1
                if 0 <= indice < len(usuarios):
                    del usuarios[indice]
                    print('Usuário deletado com sucesso!')
                else:
                    print("Índice de usuário inválido!")
            except ValueError:
                print('Entrada inválida! Informe números corretamente.')
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
        case '6':
            print('Saindo do programa.')
            break
        case _:
            print('Opção inválida! Tente novamente.')
