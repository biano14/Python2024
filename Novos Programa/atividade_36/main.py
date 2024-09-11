import random

class Pessoa:
    def __init__(self, nome, humor):
        self.humor = humor
        self.nome = nome
    
    # método de ação
    def cumprimentar(self):
        if self.humor:
            print(f'olá, meu é {self.nome}. Qual o seu?')
        else:
            print('Se liga meu irmão, pega andando !!')

    def responder(self, nome, humor):
        if humor:
            print(f'Oi, {nome}, meu nome {self.nome}. É uma satisfação te conhecer. ')
            self.humor = True

        else:
            print('Vai se fuder, desgrama.')
            self.humor = False
        return self.humor
    

if __name__ == '__main__':
    humores = (True, False)
    nome1 = input('Informe o nome do 1ª pessoa:')
    nome2 = input('Informe o nome do 2º pessoa:')

    # instância dos objetos
    user1 = Pessoa(nome1, humores[random.randint(0,1)])
    user2 = Pessoa(nome2, humores[random.randint(0,1)])

    user1.cumprimentar()
    user1.humor = user2.responder(user1.nome, user2.humor)

    if user1.humor:
        print(f'{user1.nome} ficou alegre.')
    else:
        print(f'{user1.nome} ficou puto.')