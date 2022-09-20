

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mVALOR INVÁLIDO TENTE NOVAMENTE!!\33[m')
        if ok:
            break
    return valor


from arquivos_recepcao.utilidades import arquivo_STR

print('''\033[1;34mAgradecemos o contato e seguem as informações das diárias para efetivação da reserva.
Estamos localizados no centro de Joaçaba, com excelente infraestrutura para SERVIR BEM.
      
            Informações Adicionais:
       
                APTOS EXECUTIVOS:
Esta é a opção ideal para àqueles que precisam de conforto e praticidade. São apartamentos equipados 
com TV a cabo 32 polegadas LCD, telefone, frigobar, cama box e ar condicionado de janela e estão 
localizados do 1º ao 3º andar. 
                APTO SUPERIOR:
Destinados aos clientes que buscam apartamento ainda mais diferenciado. São equipados com TV a cabo 32 polegadas LCD,
telefone, frigobar, ar condicionado split, camas box, secador de cabelo e estão localizados do 4º ao 6º andar.

• Incluso café da manhã cortesia, quando servido no salão do café das 06h00min às 10h00min;
• Incluso uso de sauna úmida e seca;
• Piscina térmica;
• Fitness Center;
• Business Center com internet;
• Aptos com acesso Wireless
• Sala de jogos;
• Lavanderia com room service;
• Dispomos de massoterapeuta terceirizada R$85,00 uma hora de massagem;
• Não cobramos taxa de serviço;
• Garagem coberta monitorada e terceirizada R$18,00
\033[m''')
aptos = ["Single", 252.00, "Duplo ou casal", 310.00, "Conj.Triplo",
         450.00, "Conj.Quádruplo", 555.00]
aptsup = ["Single", 310.00, "Duplo ou casal", 398.00, "Conj.Triplo",
          535.00, "Conj.Quádruplo", 635.00, "Suíte single", 410.00, "Suíte Casal", 450.00]
economico = ["Single", 120.00, "Duplo ou casal", 190.00, "Conj.Triplo",
             270.00, "Conj.Quádruplo", 320.00]
print('APTOS EXECUTIVOS'.center(30))
print('-' * 35)
for pos in range(0, len(aptos)):
    if pos % 2 == 0:
        print(f'{aptos[pos]:.<20}', end=' ')
    else:
        print(f'R${aptos[pos]:>6.2f}')
print('')
print('-' * 35)
print('APTOS SUPERIOR'.center(30))
print('-' * 35)
for pos in range(0, len(aptsup)):
    if pos % 2 == 0:
        print(f'{aptsup[pos]:.<20}', end='')
    else:
        print(f'R${aptsup[pos]:.>6.2f}')
print('')
print('-' * 35)
print('APTOS ECONÔMICOS'.center(30))
print('-' * 35)
for pos in range(0, len(economico)):
    if pos % 2 == 0:
        print(f'{economico[pos]:.<20}', end='')
    else:
        print(f'R${economico[pos]:.>6.2f}')
print('')
desconto = leiaInt('\033[1;31mVALOR DO DESCONTO ( % ):\033[m ')
# DESCONTOS DOS APTOS EXECUTIVOS
print(f'\033[1;34mAPTOS EXECUTIVOS COM DESCONTO DE {desconto:.0f} %\033[m')
singleex = aptos[1] - (aptos[1] * desconto / 100)
duploex = aptos[3] - (aptos[3] * desconto / 100)
triploex = aptos[5] - (aptos[5] * desconto / 100)
quadruploex = aptos[7] - (aptos[7] * desconto / 100)
print(f'{aptos[0]}................R${singleex:.2f}')
print(f'{aptos[2]}........R${duploex:.2f}')
print(f'{aptos[4]}...........R${triploex:.2f}')
print(f'{aptos[6]}........R${quadruploex:.2f}')
print('')
print('')
# DESCONTOS DOS APTOS SUPERIORES
print(f'\033[1;34mAPTOS SUPERIOR COM DESCONTO DE {desconto:.0f}%\033[m')
singlesup = aptsup[1] - (aptsup[1] * desconto / 100)
duplosup = aptsup[3] - (aptsup[3] * desconto / 100)
suptriplo = aptsup[5] - (aptsup[5] * desconto / 100)
supquadruplo = aptsup[7] - (aptsup[7] * desconto / 100)
suitsingle = aptsup[9] - (aptsup[9] * desconto / 100)
suitduplo = aptsup[11] - (aptsup[11] * desconto / 100)
print(f'{aptsup[0]}................R${singlesup:.2f}')
print(f'{aptsup[2]}........R${duplosup:.2f}')
print(f'{aptsup[4]}...........R${suptriplo:.2f}')
print(f'{aptos[6]}........R${supquadruplo:.2f}')
print(f'{aptsup[8]}..........R${suitsingle:.2f}')
print(f'{aptsup[10]}...........R${suitduplo:.2f}')
print('')
print('')
arquivo_STR.data()
print('''Atenciosamente,
Isaias Batista
Recepcionista
HOTEL JARAGUÁ REAL
REAL HOTELARIA LTDA
Contato : (49) 3527-7300
recepcao@hoteljaraguareal.com.br
jaragua@hoteljaraguareal.com.br''')
print('http://www.hoteljaraguareal.com.br')
