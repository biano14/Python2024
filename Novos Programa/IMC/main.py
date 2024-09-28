while True:
    nome = input('Informe seu nome: ')
    altura = float(input('Informe sua altura (em m): ').replace(',', '.'))
    peso = float(input('Informe seu peso (em kilo): ').replace(',', '.'))

    imc = peso / (altura ** 2)
    
    if imc < 17:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Muito abaixo do peso ideal")
    elif imc <= 18.5:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Abaixo do peso ideal")
    elif imc <= 24.99:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Peso ideal")
    elif imc <= 29.99:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Sobrepeso")
    elif imc <= 34.99:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Obesidade grau I")
    elif imc <= 39.99:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Obesidade grau II")
    else:
        print(f"Olá {nome}, seu IMC é {imc:.2f}, seu diagnóstico é: Obesidade grau III")

    continuar = input('Deseja fazer novo cálculo? (s/n): ').lower()
    if continuar != 's':
        print('Programa finalizado')
        break
