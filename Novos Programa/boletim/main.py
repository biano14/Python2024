nome = input('Informe o nome do aluno: ')
nota = str(input('Informe a nota final: ')).replace(',','.')

#conversão
nota = float(nota)

# verificação se o aluno passou ou não
if nota <= 10 and nota >= 0:
    if nota >= 7:
        print (f'{nome} está aprovado.')
    elif nota >= 5:
        print (f'{nome} está de recuperação.')
    else:
        print (f'{nome} está reprovado.')
else:
    print('Nota inválida.')