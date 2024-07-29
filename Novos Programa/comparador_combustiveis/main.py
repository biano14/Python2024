etanol = str(input('Informe o valor do etanol: ')).replace(',','.')
gasolina = str(input('Informe o valor da gasolina: ')).replace(',','.')

#conversão
etanol = float(etanol)
gasolina = float(gasolina)

# verificação de qual combustivel mais vantajoso

if etanol > 0.70 * gasolina:
    print('Gasolina é mais vantajosa')
else:
    print('Etanol é mais vantajoso')