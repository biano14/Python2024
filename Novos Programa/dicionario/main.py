usuario = {'nome': 'Gustavo Fabiano'
           ,'idade': 27,
            'profissão': 'programador'
}
print(usuario)

#adicionar uma nova chave
#usuario['email'] = 'biano@duck'
usuario['email'] = input('Digite seu email: ')

#Alterar nome
usuario['nome'] = input('Digite o novo nome: ')
#exibindo valores do dicionario na tela
#print(usuario.get('nome'))
#print(usuario.get('idade'))
#print(usuario.get('profissão'))
#print(usuario.get('email'))

# excluindo a chave
del usuario[input('Informe a chave a ser excluida: ')]
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')
