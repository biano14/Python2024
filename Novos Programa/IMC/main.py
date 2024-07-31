while True:
# entrada de dados
    nome = input('Informe seu nome: ')
    altura = float(input('Informe sua altura (em m): ').replace(',','.'))
    peso = float(input('Informe seu peso (em kilo): ').replace(',','.'))

    imc = peso/(altura*altura)
    
    if imc < 17:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Muito abaixo do peso ideal")
    elif imc <= 18.5:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Abaixo do peso ideal")
    elif imc >= 18.51 and imc <= 24.99:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Peso ideal")
    elif imc >= 25 and imc <= 29.99:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Sobrepeso")
    elif imc >= 30 and imc <= 34.99:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Obesidade grau I")
    elif imc >= 35 and imc <= 39.99:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Obesidade grau II")
    elif imc >40:
        print(f"Olá {nome} , seu IMC é {str(imc)} , seu diagnóstico é: Obesidade grau III")
    continuar = input('Deseja fazer novo calculo? (s/n)').lower()
    if continuar == 's' :
        continue
    else:
        print('Programa finalizado')
        break            