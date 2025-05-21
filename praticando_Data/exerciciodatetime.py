from datetime import datetime
from zoneinfo import ZoneInfo


# criando um script de 30 dias diente a data q foi dada e fazendo um sistema condicional 
ultima_compra = datetime(2023,5,10)
data_hora_agora = datetime.now()
print(ultima_compra)
print(data_hora_agora)

diferenca = data_hora_agora - ultima_compra
if diferenca.days > 30 :
    print("Parabéns você ganhou um desconto!!")


# aplicar para tres fuso horarios diferentes 

fuso_horario_saopaulo = ZoneInfo("America/Sao_Paulo")
fuso_horario_ny = ZoneInfo("America/New_York")
fuso_horario_toquio = ZoneInfo("Asia/Tokyo")

data_hora_saopaulo = data_hora_agora.astimezone(fuso_horario_saopaulo)
data_hora_ny = data_hora_agora.astimezone(fuso_horario_ny)
data_hora_toquio = data_hora_agora.astimezone(fuso_horario_toquio)

print(f"Data/Hora em São Paulo: {data_hora_saopaulo}")
print(f"Data/Hora em Nova York: {data_hora_ny}")
print(f"Data/Hora em Toquio: {data_hora_toquio}")

def verificar_horario(data_hora):
    if 9 >= data_hora.hour < 17:
        return "aberto"
    else:
        return "fechado"
    
print(f"O escritorio esta de São Paulo está {verificar_horario(data_hora_saopaulo)}")
print(f"O escritorio esta de Nova York está {verificar_horario(data_hora_ny)}")
print(f"O escritorio esta de Tóquio está {verificar_horario(data_hora_toquio)}")