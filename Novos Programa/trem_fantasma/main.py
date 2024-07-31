# entrada de dados
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
altura = str(input('Informe sua altura: ')).replace(',','.')

#converte altura para float
altura = float(altura)

# verificação da idade e altura
if idade >= 12 and altura >= 1.10:
    print(f'{nome} está autorizado')
else: 
    print(f'{nome} não está autorizado.')