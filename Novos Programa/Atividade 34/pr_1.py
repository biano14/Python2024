try:
    numero = float(input("Informe um número: ").replace(",","."))
    print(f"Número : {numero}")
    print(type(numero))
except:
    print("Valor digitado inválido")