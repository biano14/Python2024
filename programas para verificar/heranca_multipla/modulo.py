class Pai:
    def __init__(self, nome, email, profissao):
        self.__nome = nome
        self.__email = email
        self.__profissao = profissao

# metodos de acesso
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def profissao(self):
        return self.__profissao


    @nome.setter
    def profissao(self, profissao):
        self.__profissao = profissao
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def nome(self, email):
        self.__email = email
        
    def exibir_fisico(self):
        print(f'Nome: {self.__nome},')
        print(f'Email: {self.__email}.')
        print(f'Profissão: {self.__profissao}.')
class Mae:
    def __init__(self,olhos, peso, altura, cor_cabelo):
        self.__olhos = olhos
        self.__peso = peso
        self.__altura = altura
        self.__cor_cabelo = cor_cabelo
        
    #metodos de acesso
    @property
    def olhos(self):
        return self.__olhos
        
    @olhos.setter
    def olhos(self, olhos):
        self.__olhos = olhos
        
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
        
    @property
    def altura(self):
        return self.__altura
        
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        
    @property 
    def cor_cabelo(self):
        return self.__cor_cabelo
        
    @cor_cabelo.setter
    def cor_cabelo(self, cor_cabelo):
        self.__cor_cabelo = cor_cabelo
            
    @property
    def olhos(self):
        return self.__olhos
        
    @olhos.setter
    def olhos(self, olhos):
        self.__olhos = olhos
    
    def exibir_fisico(self):
        print(f'Cor dos olhos: {self.__olhos},')
        print(f'Peso: {self.__peso}.')
        print(f'Altura: {self.__altura}.')
        print(f'Cor do cabelo: {self.__cor_cabelo}.')