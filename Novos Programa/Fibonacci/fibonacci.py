def calcula_fibonacci (n):
    if n <= 1:
        return 1
    else:
        return calcula_fibonacci(n-2) + calcula_fibonacci(n-1)
def verifica_inteiro(entrada):
    while True:    
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
if __name__ == '__main__':
    while True:
        entrada = input("Informe o valor inteiro positivo para a sequência de Fibonacci: ")
        try:    
            for i in range(int(entrada)):
                contador = i
                print(calcula_fibonacci(contador))
                contador =- 1
            
            repetir = input('Deseja gerar outro sequência (s/n): ').lower()
            if repetir == 's':
                continue
            else:
                break 
        except:
            print('Valor informado inválido')
