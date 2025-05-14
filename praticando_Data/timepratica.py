'''usando as abreviacoes d e dia b e mes y e ano usando a % mas a letra a letra minuscula e abreviacoes e maiuscula e nome completo '''
import locale
import time

#definir a localização em portugues 
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()


print(tempo_em_struct)

print(time.strftime("%d %B %Y" , tempo_em_struct))

print(time.strftime("%H:%M:%S", tempo_em_struct))


## Tempo formatado o A significa dia da semana

tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S",tempo_em_struct)
print(f" Tempo formatado {tempo_formatado}")

