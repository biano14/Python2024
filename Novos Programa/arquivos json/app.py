import os
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    #instancia os objetos
    p = Pessoa(0,'','','','')
    m = Manipulador()
    
    while True:
        print('1 - Criar novo arquivo JSON.')
        print('2 - Abrir e Ler arquivo JSON')
        print('0 - Sair do programa.')
        opcao = input('Informe a opção desejado: ')
        
        #limpeza de console
        os.system('cls')
        
        match opcao:
            case '0':
                break
            case '1':
                novo_arquivo = input('Informe o nome do arquivo que deseja criar: ')
                print(m.criar_arquivo(novo_arquivo))
                continue
            case '2': 
                abrir_arquivo = input('Informe o nome do arquivo que deseja abrir: ')
                try:
                    os.system('cls')
                    usuarios = m.abrir_arquivo(abrir_arquivo)
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for i in range(len(usuarios)):
                        for campo in usuarios[i]:
                            print(f'{campo.capitalize()}: {usuarios[i].get(campo)}.')
                        print(f'\n{'-'*30}\n')
                except Exception as e:
                    print(f'Não foi possível abrir o arquivo. {e}.')
                finally:
                    continue
            case '2': 
                abrir_arquivo = input('Informe o nome do arquivo que deseja abrir: ')
                try:
                    usuario = {}
                    campos = ('nome','cpf','email','profissao')
                    print(f'Arquivo aberto {abrir_arquivo}.json.\n')
                except Exception as e:
                    print(f'Não foi possível realizar a operação. {e}.')
                finally:
                    continue
            case '_':
                print('Opção inválida.')