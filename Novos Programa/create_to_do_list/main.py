import os
# lista
tarefas = []

while True:
    print('1 - Cadastrar nova tarefa')
    print('2 - Imprimir lista de tarefas')
    print('3 - Sair do programa')
    opcao = input('\nInforme a opção desejada: ')
    os.system('cls')
    match opcao:
        case '1':
            nova_tarefa = input('\nInsira a nova tarefa: ')
            tarefas.append(nova_tarefa)
            print ('\nNova tarefa cadastrada com sucesso')
            print (f'\n"{nova_tarefa}"')
            continue
        case '2':
            print(f'{10*'-'}Lista de Tarefas{10*'-'}\n')
            for tarefa in range(len(tarefas)):
                print(f'{tarefa + 1}° tarefa: "{tarefas[tarefa]}"\n')
            continue
        case '3':
            break
        case _:
            print('Opção inválida\n')
            continue