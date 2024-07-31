import os
import time

# entrada de dados
numero = int(input('Informe um número inteiro: '))

print('\nContagem regressive: ')

#saida de dados
while numero >= 0:
    print(numero)
    numero -= 1
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')