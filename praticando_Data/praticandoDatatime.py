from datetime import datetime,timedelta


#funcao now retorna data e horas atuais 
agora = datetime.now()
print(f'Agora' , agora)

# imprimir so a data 
print(f'Data {agora.date()}')
#imprimir so a hora
print(f'Hora {agora.time()}')


#atributos 
print(f'Ano: {agora.year}')
print(f'Mês: {agora.month}')
print(f'Dia: {agora.day}')
print(f'Hora: {agora.hour}')
print(f'Minuto: {agora.minute}')
print(f'Segundo: {agora.second}')
# A classe timedelta e usada  para realizar operacoes  com datas (adicao , substituicao)
data_futura = agora + timedelta(days=10) 
print(f"Data 10 dias no futuro: {data_futura} ")

data_passado = agora - timedelta(days=10) 
print(f"Data 10 dias no no passado: {data_passado} ")

dez_horas_adiante = agora + timedelta(hours=10) 
print(f"Data 10 dias no futuro: {dez_horas_adiante} ")

#pode criar tambem uma data que vai ser colocada como ano mes dia hora minuto segundo e micro segundo e fuso

data = datetime(2025,12,11,8,30,20)
print(f"Data {data}")

dias_faltando =  data - agora
print(dias_faltando.days)


datas = [
    datetime(2024,8,19),
    datetime(2022,7,19),
    datetime(2025,3,10),
    datetime(2022,7,8),
]

datas_ordenadas = sorted(datas)

for date in datas_ordenadas:
    print(date.date())