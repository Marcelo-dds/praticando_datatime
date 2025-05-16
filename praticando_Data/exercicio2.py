import locale
import time
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
#cria um script que calcula quanto tempo falta para o fim do ano 

tempo_atual = time.localtime()

sengudos_por_minuto = 60
segundos_por_hora = 60 * sengudos_por_minuto
segundos_por_dia = 24 * segundos_por_hora




print(tempo_atual.tm_year)


tempo_ano_novo = (tempo_atual.tm_year + 1,1,1,0,0,0,0,0,0)
## mk time pega do tempo da epoch nesse caso eu perguntei quantos segundos e desse tempo ate a epoch estruturando o codigo de forma struct
segundos_restantes = int(time.mktime(tempo_ano_novo) - time.mktime(tempo_atual))
print(segundos_restantes)



dias, resto_segundos = divmod(segundos_restantes,segundos_por_dia)

print(dias)
print(resto_segundos)

hora,resto_segundos = divmod(resto_segundos,segundos_por_hora)
minutos,segundos = divmod(resto_segundos,sengudos_por_minuto)

print(hora)
print(minutos)
print(segundos)

print(f"Faltam {dias} dias, {hora} horas, {minutos} minutos e {segundos} segundos para o Ano Novo!")

