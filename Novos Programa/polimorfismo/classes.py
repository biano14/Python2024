# superclasse, classe-pai, classe base
class Pessoa:
    #atributos
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
    
    #metodo
    def motrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}.')
        print(f'Email: {self.email}.')
        print(f'Telefone: {self.telefone}.')
#subclasse, classe-filha, classe derivada Pessoa Física
class PessoaFisica(Pessoa):
    # polimorfismo do construtor
    def __init__(self, endereco, email, telefone,nome,cpf,profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super().__init__(endereco, email, telefone)
    def motrar_cartao_visitas(self):
        print(f'Nome do usuario: {self.nome}.')    
        print(f'CPF: {self.cpf}.')
        print(f'Profissão: {self.profissao}.')    
        super().motrar_cartao_visitas()

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia,razao_social,cnpj,endereco, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(endereco, email, telefone)
    def motrar_cartao_visitas(self):
        print(f'Nome da empresa: {self.nome_fantasia}.')
        print(f'Razão Social: {self.razao_social}.')
        print(f'CNPJ: {self.cnpj}.')
        super().motrar_cartao_visitas()