class Usuario:
    def __init__(self, nome, idade, documento):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Documento: {self.documento}"

class Veiculo:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Ano: {self.ano}"

class SystemLocacao:
    def __init__(self):
        self.veiculos = [Veiculo("Gol", "ABC-1234", 2002),Veiculo("Honda", "FGH-5678", 2024),Veiculo("Strada", "LMN-5894", 2015),Veiculo("Strada", "LMN-5894", 2021),Veiculo("Bid", "KOE-2136", 2018),Veiculo("Kwid", "KOP-4816", 2019)]
    def mostrar_veiculos(self):
        print("Veículos prontos para locação:")
        for i, veiculo in enumerate(self.veiculos):
            print(f"{i + 1}: {veiculo}")

    def alugar_veiculo(self):
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        documento = input("Digite seu documento: ")

        usuario = Usuario(nome, idade, documento)

        self.mostrar_veiculos()
        escolha = int(input("Indique o indíce do veículo que deseja alocar: ")) - 1

        if 0 <= escolha < len(self.veiculos):
            veiculo_escolhido = self.veiculos[escolha]
            print("\nDados da locação:")
            print(usuario)
            print(veiculo_escolhido)
        else:
            print("Opção inválida!")