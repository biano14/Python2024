from abc import ABC, abstractmethod

# Classe abstrata
class Conta(ABC):
    
    @abstractmethod
    def consultar_saldo(self):
        pass
    
    @abstractmethod
    def fazer_deposito(self, valor):
        pass
    
    @abstractmethod
    def fazer_saque(self, valor):
        pass

# Classe concreta que implementa a classe abstrata
class ContaCorrente(Conta):
    
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.__nome = nome 
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
    
    # getters e setters
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
        
    @property
    def conta(self):
        return self.__conta
    
    @conta.setter
    def conta(self, conta):
        self.__conta = conta
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # Métodos concretos
    def consultar_saldo(self):
        return self.__saldo

    def fazer_deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")
        return self.__saldo

    def fazer_saque(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")
        return self.__saldo


