#  Crie um programa em que o usuário informe uma quantidade desejada de números decimais de, no mínimo 0 e no máximo 10, e o programa calcula a média desses números.
numeros = []
while True:
        divisor = int(input('Informe uma quantidade de números decimais de 0 a 10 que deseja calcular a média: '))
        if divisor == 0:
            print('A média é igual a 0.')
            break
        elif divisor < 0 or divisor > 10:
            print('Informe um valor inteito positivo ou menor que 10.')
            continue
        else:
            soma = 0.0
            for num in range(len(numeros)):
                numeros[num] = input(f'Informe o {num + 1}° número: ')
                for num in numeros:
                    soma = float(soma + numeros[num])
                media = soma/divisor
                print(f'A média é {media}')
