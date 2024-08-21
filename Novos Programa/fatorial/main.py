def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
def verifica_inteiro(entrada):
    while True:    
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
if __name__ == '__main__':
    entrada = input("Informe o valor inteiro positivo para calcular o fatorial: ")
    try:
        print(f'O valor do fatorial de {entrada} é {fatorial(verifica_inteiro(entrada))}')
    except:
        print('Não foi possível calcular o fatorial')