# coding: iso-8859-1 -*-
def vermelho(msg):
    print('\033[1;31m', end='')
    return print(msg)


def verde(msg):
    print('\033[1;32m', end='')
    return print(msg)

def azul(msg):
    print('\033[1;34m', end='')
    return print(msg)


def amarelo(msg):
    print('\033[1;33m', end='')
    return print(msg)
#Programa principal
#from arquivos_recepcao.utilidades import cores
economico = ["Single", 120.00, "Duplo ou casal", 190.00, "Conj.Triplo",
             270.00, "Conj.Quadruplo", 320.00]
economicoduplo = ['Apto',102 , 'Apto', 116, 'Apto', 117, 'Apto',302, 'Apto',306, 'Apto', 309, 'Apto', 317, 'Apto',
                  406, 'Apto', 417, 'Apto', 602, 'Apto', 603, 'Apto', 604, 'Apto', 605, 'apto', 606, 'Apto', 610,
                  'Apto', 616, 'Apto', 617]
camaseparadas = ['Apto',303 , 'Apto', 304, 'Apto', 305, 'Apto',306, 'Apto',310, 'Apto', 316, 'Apto', 402, 'Apto',
                  403, 'Apto', 404, 'Apto', 405, 'Apto', 406, 'Apto', 409, 'Apto', 410, 'apto', 416, 'Apto', 417,
                  'Apto', 502, 'Apto', 503,'Apto', 504, 'Apto', 505, 'Apto', 506, 'Apto', 509, 'Apto', 516, 'Apto',517]
"""cores.verde('-'*30)
print('APTOS ECONÔMICOS'.center(30))
print('-'*30)
for pos in range(len(economico)):
    if pos % 2 == 0:
        print(f'{economico[pos]:.<20}', end=' ')
    else:
        print(f'{economico[pos]:>7.2f}')
print('-'*30)
print('''\033[1;34m*Aptos  definidos e limitados 
*(válido  somente as UH definidas)
*Garagem normal  R$ 18,00 terceirizada 
*Limpeza do  apto a cada 2 diárias
*sem  touca  de  banho
*sem  shampoo
*Não participa  do programa Fidelidade\033[m''')"""
vermelho('-'*38)
vermelho('LISTA DE APTOS DUPLOS'.center(38))
print('-'*38)
for pos in range(len(economicoduplo)):
    if pos % 2 == 0:
        print(f'{economicoduplo[pos]:.<10}', end='')
    else:
        print(f'{economicoduplo[pos]:.>8}')
azul('-'*38)
azul('APTOS QUE AS CAMAS PODEM SER SEPARADAS')
azul('-'*38)
for pos in range(len(camaseparadas)):
    if pos % 2 == 0:
        print(f'{camaseparadas[pos]:.<10}', end='')
    else:
        print(f'{camaseparadas[pos]:.>8}')
