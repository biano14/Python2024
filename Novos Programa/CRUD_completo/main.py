import os

# Definindo as chaves
chaves = ('Nome Completo', 'Data de Nascimento', 'CPF','Telefone', 'Profissão', 'E-mail', 'Endereço')

# Lista inicial de usuários
usuarios = [
    {
        chaves[0]: 'Gustavo',
        chaves[1]: '14/07/1997'
    }
]

while True:
    print(f'\n{10*'-'} Banco de Usuários {10*'-'}') 
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
            
            os.system('cls')  # Limpa a tela (funciona apenas em sistemas Windows)
            
            contador = 0
            for usuario in usuarios:
                if chave_procurada in usuario and usuario[chave_procurada] == informacao:
                    contador += 1

            print(f'{informacao} foi encontrado {contador} vezes.')
        case '4':
            for usuario in range(len(usuarios)):
                print(f'{usuario + 1}° usuário: {usuarios[usuario]}')
        case '5':
            print('Funcionalidade ainda não implementada.')
        case '6':
            print('Saindo do programa.')
            break
        case _:
            print('Opção inválida! Tente novamente.')