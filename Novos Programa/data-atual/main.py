#importando biblioteca
from calendar import month
from datetime import date

#declaração de variveis
dia = date.today().day
mes = date.today().month
ano = date.today().year

meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

print(f'Data atual: {dia} de {meses[mes - 1]} de {ano}')