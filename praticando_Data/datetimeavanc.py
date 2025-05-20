import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')

agora = datetime.now()

print(agora.strftime(""))

data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")

print(data_formatada)

string_data = "17 março, 2025, 19:10:13"
formato = "%d %B, %Y, %H:%M:%S"

data = datetime.strptime(string_data, formato)
print(f"Data {data}")

#fuso horario 
'''
from datetime import datetime,timezone

fuso_horario = timezone.utc

data_hora = datetime(12,23,45, tzinfo=fuso_horario)

print(f"DATA / hora {data_hora}")
'''