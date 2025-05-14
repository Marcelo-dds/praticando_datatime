import time ; 

''' a função time.time() retorna quantos segundos se passou desde a EPOCH que e 1 de janeiro de 1970 esse e o marco zero desse  modulo .

a função ctime() retorna a data em tipo string'''

segundos_hoje = time.time()
print(segundos_hoje)
# retorno dessa operação '1747236891.5197663'

data_hoje =  time.ctime()
print(data_hoje)
# retorno dessa operação 'Wed May 14 12:37:56 2025'


#pra esperar um tempo nesse caso 5 segundos 
print("começando")
time.sleep(5)
print("Rodou 5 segundos depois ")

# gmtime da o padrao utc ja o localtime da a hora local 
geral_hora = time.gmtime()
print(geral_hora)

local_hora = time.localtime()
print(local_hora)

'''o interresante e que pode pegar qualquer parametro '''

dia = local_hora.tm_mday
mes = local_hora.tm_mon
ano = local_hora.tm_year
dia_da_semana = local_hora.tm_wday

print(f"Data {dia},{mes},{ano} e {dia_da_semana}")