import os
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
while True:
# entrada de dados
   

    print(f'\n{'='*10} Olá {nome}, bem vindo ao cinema Senai {'='*10}')
    print('1 - Deadpool & Wolverine - Sala 1 (18 anos)')
    print('2 - Divertida Mente 2 - Sala 2 (Livre)')
    print('3 - Twisters - Sala 3 (12 anos)')
    print('4 - Bad Boys  Ride or Die - Sala 4 (16 anos)')
    print('5 - A Quiet Place: Day One - Sala 5 (14 anos)')
    opcao = input('\nEscolha o filme que deseja assistir: ')
    match opcao:
        case '1': 
            if int(idade) < 18:
                os.system('cls')
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitido')
                break
        case '2': 
            print('Ingresso emitido')
            break
        case '3': 
            if int(idade) < 12:
                os.system('cls')
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitido')
                break 
        case '4': 
            if int(idade) < 16:
                os.system('cls')
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitido')
                break
        case '5': 
            if int(idade) < 14:
                os.system('cls')
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitido')
                break
        case _:
            os.system('cls')
            print('Sala inexistente. Favor escolher outra sala.')     