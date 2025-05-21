from datetime import datetime

# um usuario coloca a data de nascimento dele e partir dessa data calcula quantos anos ele tem 


data_nascimento_usuario = input("Informe Data de nascimento (dd/mm/aaaa): ")

data_nascimento_usuario_criptografado = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")

data_atual = datetime.now()

idade = data_atual.year - data_nascimento_usuario_criptografado.year

mes_atual = data_atual.month
dia_atual = data_atual.day

mes_nascimento = data_nascimento_usuario_criptografado.month
dia_nascimento = data_nascimento_usuario_criptografado.day

if mes_nascimento > mes_atual:
    idade-= 1 
elif mes_nascimento == mes_atual and dia_atual < dia_nascimento:
    idade -= 1

print(f"Sua idade é {idade} Anos")