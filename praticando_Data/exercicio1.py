import time
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
# exercio de contagem regrssiva 

'''for numero in range(10,0,-1):
    print(numero)
    time.sleep(1)
print("O Evento começou!!!")

#outro modo sem pular linha 
for numero in range(10,0,-1):
    print(numero, end=" \r")
    time.sleep(1)
print("O Evento começou!!!")
'''

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime('%A, %d de %B de %Y, %H:%M',tempo_em_struct)
print(tempo_formatado)