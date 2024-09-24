from dataclasses import dataclass

# Criar a classe pessoa
@dataclass
class Pessoa:
    nome: str
    cpf: str
    email: str
    profissao: str

    # Destrutor
    def __del__(self):
        return f"Objeto{self.nome} destruido."