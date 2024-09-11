import classes as cl

if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome do usúario: ')
    email = input('Informe o email do usúario: ')
    cpf = input('Informe o CPF do usúario: ')
    profissao = input('Informe o profissão do usúario: ')
    endereco = input('Informe o endereço do usúario: ')
    telefone = input('Informe o telefone do usúario: ')
    
    #instancia a classe pessoa física
    usuario = cl.PessoaFisica(endereco,email,telefone,nome,cpf,profissao)
    
    #entrada de dadps
    nome = input('Informe o Nome Fantasia da empresa: ')
    email = input('Informe o email da empresa: ')
    cnpj = input('Informe o CNPJ da empresa: ')
    razao_social = input('Informe a razão social da empresa: ')
    endereco = input('Informe o endereço da empresa: ')
    telefone = input('Informe o telefone da empresa: ')
    
    #instacia a classe pessoa juridica
    empresa = cl.PessoaJuridica(nome,razao_social,cnpj,endereco,email,telefone)
    
    #saida de dados
    usuario.motrar_cartao_visitas()
    print('-'*10)
    empresa.motrar_cartao_visitas()