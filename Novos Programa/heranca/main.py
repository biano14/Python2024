
# Classe Pai
class Pessoa:
    # atributos
    cidade = "Brasília"
    telefone = "(61) 98107-1050"
    email = "nome@gmail.com"

# subclasse (classe-filha)
class PessoaFisica(Pessoa):
    #atributos
    nome = "Fulano de Tal"
    cpf = "123.123.123-00"
    peso = 90
    altura = 1.85

class PessoaJuridica(Pessoa):
    #atributos
    nome_fantasia = "Cobra Kai"
    razao_social = "Fulano de Tal S.A."
    cnpj = '28.994.543/0001-90'

# programa principal
if __name__ == '__main__':
    # instacia dos objetos
    usuario = PessoaFisica()
    empresa = PessoaJuridica()

    print(f'{'-'*30} DADOS DO USUÁRIO {'-'*30}\n')
    print(f'Nome do Usuário: {usuario.nome}')
    print(f'CPF do Usuário: {usuario.cpf}')
    print(f'Peso do Usuário: {usuario.peso}')
    print(f'Altura do Usuário: {usuario.altura}')
    print(f'Cidade onde o Usuário mora: {usuario.cidade}')
    print(f'Telefone do Usuário: {usuario.telefone}')
    print(f'E-mail do Usuário: {usuario.email}')
    
    print(f'\n{'>'*30} DADOS DO USUÁRIO {'<'*30}\n')
    print(f'Nome do Empresa: {empresa.nome_fantasia}')
    print(f'Razão social da Empresa: {empresa.razao_social}')
    print(f'CNPJ da Empresa: {empresa.cnpj}')
    print(f'Cidade sede da Empresa: {empresa.cidade}')
    print(f'Telefone da Empresa: {empresa.telefone}')
    print(f'E-mail da Empresa: {empresa.email}')