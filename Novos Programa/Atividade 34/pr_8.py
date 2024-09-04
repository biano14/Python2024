#  Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.
def calcular_media(divisor, numeros):
    while True:
        if 0 < divisor <= 10:      
                    soma = 0.0
                    for num in range(divisor):
                        valor = input(f'Informe o {num + 1}° número: ').replace(',','.')
                        numeros.append(float(valor))
                        soma = float(soma + numeros[num])
                    media = soma/divisor
                    print(f'A média é {media}')
                    break
        elif divisor < 0:
            print('Informe um valor maior que 0')
            divisor = int(input('Informe uma quantidade de números decimais de 0 a 10 que deseja calcular a média: '))
            continue
        else:
            print('Informe um valor menor que 10 e/ou valor válido.')
            divisor = int(input('Informe uma quantidade de números decimais de 0 a 10 que deseja calcular a média: '))
            continue
numeros = []

divisor = int(input('Informe uma quantidade de números decimais de 0 a 10 que deseja calcular a média: '))
calcular_media(divisor, numeros)

