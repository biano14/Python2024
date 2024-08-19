import calendar
from datetime import date

for mes in range(12):
    print(calendar.month(date.today().year, mes + 1))