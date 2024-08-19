import time

msgs = ('Abrindo program...', 'Executando programa...', 'Ainda executando o programa...', 'Programa demorando mais que o esperado...', 'Finalizando. Aguarde...', 'Programa executado e finalizado com sucesso.')

for msg in msgs:
    print(msg)
    time.sleep(3)