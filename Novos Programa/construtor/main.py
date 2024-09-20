# NOTE: cria a classe
class Pessoa:
    # os atributos são SEMPRE definidos dentro do método construtor
    # NOTE: método construtor
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
    
# NOTE: progama principal:
if __name__ == '__main__':
    nome = input('Informe o nome do usúario: ')
    idade = input('Informea idade do usúario: ')
    cpf = input('Informe o cpf do usúario: ')
    email = input('Informe o email do usúario: ')
    
#instancia o objeto
usuario = Pessoa(nome, idade, cpf, email)

#saída de dados
print(f'Nome: {usuario.nome}.')
print(f'Idade: {usuario.idade}.')
print(f'CPF: {usuario.cpf}.')
print(f'E-mail: {usuario.email}.')