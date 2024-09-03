try:
    num = int(input("Informe um número inteiro: "))
    resto = num % 2 
    if resto == 0 or num == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é impar.")
except:
    print("Valor informado inválido.")   