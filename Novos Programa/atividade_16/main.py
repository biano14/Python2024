import os
usuario = {}

usuario['Nome'] = input('Informe o nome a pessoa a ser cadastrada: ')
os.system('cls')
usuario['Sexo'] = input('Informe o genêro da pessoa a ser cadastrada: ')
os.system('cls')
usuario['CPF'] = input('Informe o CPF da pessoa a ser cadastrada: ')
os.system('cls')
usuario['RG'] = input('Informe o RG da pessoa a ser cadastrada: ')
os.system('cls')
usuario['Data de Nascimento'] = input('Informe a data de nascimento: ')
os.system('cls')
usuario['Signo'] = input('Informe o signo: ')
os.system('cls')
usuario['Mãe'] = input('Informe o nome da mãe: ')
os.system('cls')
usuario['Pai'] = input('Informe o nome do pai: ')
os.system('cls')
usuario['Email'] = input('Informe o email: ')
os.system('cls')
usuario['Senha'] = input('Informe o senha do email: ')
os.system('cls')
usuario['CEP'] = input('Informe o CEP: ')
os.system('cls')
usuario['Endereço'] = input('Informe o Endereço: ')
os.system('cls')
usuario['Número'] = input('Informe o número do Endereço: ')
os.system('cls')
usuario['Bairro'] = input('Informe o bairro do Endereço: ')
os.system('cls')
usuario['Cidade'] = input('Informe a Cidade: ')
os.system('cls')
usuario['Estado'] = input('Informe o Estado: ')
os.system('cls')
usuario['Telefone'] = input('Informe o Telefone: ')
os.system('cls')
usuario['Celular'] = input('Informe o Celular: ')
os.system('cls')
usuario['Altura'] = input('Informe a Altura: ')
os.system('cls')
usuario['Peso'] = input('Informe o Peso: ')
os.system('cls')
usuario['Tipo Sanguineo'] = input('Informe seu Tipo Sanguineo: ')
os.system('cls')
usuario['Cor'] = input ('Informe a Cor Favorita: ')
os.system('cls')

#exigir o dicionario
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')

