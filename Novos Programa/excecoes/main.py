# entrada de dados
x = input('Informe um número: ')
y = input('Informe outro número: ')

#tratamento de exceção
try :
# multiplicação os números
    multiplicacao = int(x) * int(y)

# exibe o resultado na tela
    print (f'O resultado da multiplicação é {multiplicacao}.')

except:
    print('Não foi possível realizar o cálculo.')