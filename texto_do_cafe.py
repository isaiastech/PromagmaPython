from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%Y')
print(f'      \033[1;32m {hora}')
escolha = int(input('''1- CAFÉ COLONIAL
2- CAFÉ DA MANHÃ 
ESCOLHA UMA OPÇÃO: '''))
print('-='*20)
cafe = str(input('Digite o nome do cliente do café: ')).strip().title()
data = str(input('Data da reserva : '))
if escolha == 1:
    print(f"\033[1;32mBoa noite, segue em anexo a reserva do café colonial em nome de: {cafe} \npara {data}.")
else:
    print(f"\033[1;32mBoa noite, segue em anexo a reserva do café da manhã em nome de: {cafe} \npara {data}.")
print('')
print('''Atenciosamente!
Isaias Batista
Recepcionista
HOTEL JARAGUÁ REAL
REAL HOTELARIA LTDA
Contato : (49) 3527-7300
recepcao@hoteljaraguareal.com.br
jaragua@hoteljaraguareal.com.br''')
