from cinematica import * 

while True:
    mostrar_menu()

    opcao = input('Opção do usuário: ')

    match opcao:
        case '1':
            m = float(input('Informe a massa em kg: ').replace(',','.'))
            h = float(input('Informe a altura em metros: ').replace(',','.'))
            print(f'Energia potêncial: {calcular_ep(m,h)}.')
            continue
        case '2':
            m = float(input('Informe a massa em kg: ').replace(',','.'))
            v = float(input('Informe a velociade em m/s: ').replace(',','.'))
            print(f'Energia cinética: {calcular_ac(m,v):,.2f}.')
            continue
        case '3':
            break
        case _:
            print('Opção inválida')
            continue
