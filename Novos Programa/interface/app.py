from modulo import ContaCorrente
# completem o programa: o usuario vai informar o nome e o CPF, e o programa informa a agencia, conta e saldo. e ai o usuario cai pode escolher se deseja fazer saque, deposito ou sair do programa 
if __name__ == "__main__":
    # Recebendo as informações do usuário
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    
    # Criando a conta corrente
    cc = ContaCorrente(nome, cpf, '1010-1','10010-1', 0)
    
    while True:
        print("\nMenu:")
        print("1. Consultar saldo")
        print("2. Fazer depósito")
        print("3. Fazer saque")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print(f"Saldo atual: R$ {cc.consultar_saldo():.2f}")
        
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor do depósito: R$ "))
                cc.fazer_deposito(valor)
                print(f"Novo saldo: R$ {cc.consultar_saldo():.2f}")
            except ValueError:
                print("Valor inválido. Digite um número.")
        
        elif opcao == '3':
            try:
                valor = float(input("Digite o valor do saque: R$ "))
                cc.fazer_saque(valor)
                print(f"Novo saldo: R$ {cc.consultar_saldo():.2f}")
            except ValueError:
                print("Valor inválido. Digite um número.")
        
        elif opcao == '4':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


