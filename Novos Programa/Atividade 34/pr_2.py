try:    
    peso = int(input("Informe o peso em gramas do recém-nascido: ").replace(",","."))
    if peso >= 2500:
        print("O bebê está saudável.")
    else:
        print("O bebê precisa ser internado.")
except:
    print("Valor informado inválido")