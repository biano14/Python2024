# Lista de Dicionario
chaves = ('Nome', 'Idade', 'Profissão')

usuarios = [
    {
        chaves[0]: 'Fulano',
        chaves[1]: 20,
        chaves[2]: 'Programador'
    },
    {
        chaves [0]: 'Cicrano',
        chaves [1]: 35,
        chaves [2]: 'Analista'
    },
    {
        chaves[0]: 'Beltrano',
        chaves[1]: 45,
        chaves[2]: 'Faxineira'
    }
]
print(f'\n{'='*10} LISTA DE USUARIOS {'='*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{'-'*10}\n')  

# adicionar novo dicionario a lista

for i in range(len(chaves)):
    usuario[chave[i]] = input(f'Informe o/a {chave[i]}')
usuario  