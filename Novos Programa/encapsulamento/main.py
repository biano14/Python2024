import classe as cl
if __name__ == '__main__':
    #entrada de dados
    nome = input('Informe o nome: ')
    idade = int(input('Informe sua idade: '))
    email = input('Informe seu email: ')
    
    # Instancias da classe:
    usuario = cl.Pessoa(nome, idade, email)
    
    # Saída de Dados
    print(f'Nome: {usuario.nome}')
    print(f'Idade: {usuario.idade}')
    print(f'E-mail: {usuario.email}')