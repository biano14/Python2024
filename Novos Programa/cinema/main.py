nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
while True:
# entrada de dados
   

    print(f'\n{'='*10} Olá {nome}, bem vindo ao cinema Senai {'='*10}')
    print('1 - Deadpool & Wolverine - Sala 1 (18 anos)')
    print('2 - Divertida Mente 2 - Sala 2 (Livre)')
    print('3 - Twisters - Sala 3 (12 anos)')
    print('4 - Bad Boys - Ride or Die (16 anos)')
    print('5 - A Quiet Place: Day One (14 anos)')
    print(f'{54*'='}')
    opcao = input('\nEscolha o filme que deseja assistir: ')
    match int(opcao):
        case 1: 
            if int(idade) < 18:
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitidido')
                break
        case 2: 
            print('Ingresso emitidido')
            break
        case 3: 
            if int(idade) < 12:
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitidido')
                break 
        case 4: 
            if int(idade) < 16:
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitidido')
                break
        case 5: 
            if int(idade) < 14:
                print('\nVocê não tem idade para assistir esse filme. Selecione outro filme')
            else:
                print('Ingresso emitidido')
                break      