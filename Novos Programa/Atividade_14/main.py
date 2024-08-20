
notas = []

while True:
    print(f'{10*'-'}Media de Notas{10*'-'}')
    print('1 - Inserir nota.')
    print('2 - Calcular média das notas.')
    print('3 - Sair do programa.')

    opcao = input('Opção: ')

    match opcao:
        case '1':
            nova_nota = str(input('Informe uma nota de 0 a 10: ')).replace(',','.')

            try:
                nova_nota = float(nova_nota)
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print(f'Nota {nova_nota} inserida com sucesso')
                else:
                    print('Nota inválida')
            except:
                print('Não foi possível inserir a nova nota')
            finally:
                continue
        case '2':
            try:
                media = sum(notas) / len(notas)
                print(f'A média do aluno é {media:,.2f}.')
            except:
                print('Não foi possível calcular a média')
            finally:
                continue
        case '3':
            print('Programa encerrado')
            break
        case _:
            print('Opção inválida.')
            continue