from calendar import month
from datetime import date
chaves = ('Nome do evento','Classificação')
eventos = []
def verifica_idade(opcao):
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    while True:
        try:
            print(f'\n{"="*10} EVENTOS EM EXIBIÇÃO {"="*10}\n')
            for i, evento in enumerate(eventos):
                print(f'{i + 1}° evento:{evento}')
                print(f'\n{"-"*10}\n')
            escolha = int(input('Selecione o evento que deseja ir: '))
            if escolha <= len(eventos) and escolha > 0:
                if idade < int(eventos[escolha - 1][chaves[1]]):
                    print('Entrada Proibida. Escolha outro evento.')
                else:
                    print(f'Aqui está seu ingresso')
                    print('\n')
                    print(f'Nome: {nome}')
                    print(f'{evento[escolha - 1]}')
                    print(f'Ingresso emitido em: {dia} de {meses[mes - 1]} de {ano}')
                    break
            else:
                print('Informe um evento valido')
        except:
            print('Valor inválido inserido')

while True:
    evento = {}
    for chave in chaves:
        evento[chave] = input(f'Informe o/a {chave.lower()}: ')
    eventos.append(evento)
    print('\nEvento cadastrado com sucesso!')
    opcao = input('Deseja cadastrar outro evento (s/n): ')
    if opcao == 'n':
        nome = input('Informe seu nome: ')
        idade = int(input('Informe sua idade: '))
        verifica_idade(opcao)
        break
    else:
        continue