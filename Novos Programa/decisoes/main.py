# entrada de dados
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')

# verifição da idade
try:
#conversão para int
    idade = int(idade) 
#     
    if idade >= 18:
        print(f'{nome} é maior de idade.')
    else:    
        print(f'{nome} é menor de idade.')
except ValueError:
    print("Por favor, insira um número válido.")