lista = ['Gustavo', 'Pedro', 'João', 'Maria', "Fernanda", 'Joaquim', 'Marcelo', 'Thabata','Laisa','Ana']
try:
    indice = int(input("Informe o indice do nome da lista que deseja exibir: " ))
    print(f"Nome correspondente ao indice: {lista[indice - 1]}")
except:
    print("Valor informado inválido.")