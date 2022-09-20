# -*- encoding: utf-8 -*-
#Programa criado em 05/07/2020
from datetime import datetime
dia = datetime.now()
dia = dia.strftime('%d/%m/%Y')
print('-'*38)
print(f'{dia}'.center(38))
print('-'*38)
cartao = open('cartao.txt', 'a')
apto = []
cabacalho = str('APTO')
cabacalho2 = str('DATA')
falta = int(input('Total de cartões faltando? '))
cobrados = int(input('Quantidade de cartões cobrados? '))
cobrados2 = cobrados * 10
print('-'*38, )
while True:
    apto.append(str(input('Qual apto foi cobrado? ')))
    apto.append(str(input('Qual a data? ')))
    res = str(input('Quer continuar [S/N]? ')).upper()[0]
    if res in 'N':
        break
print('RELATÓRIO DE CARTÕES'.center(30), file=cartao)
print('-'*30, file=cartao)
print(f'{dia} está faltando {falta}', file=cartao)
print(f'Os cartões cobrados foram {cobrados}', file=cartao)
print(f'O valor recebido foi R${cobrados2:.2f}', file=cartao)
print(f'TEVE DE REEMBOLSO PARA O HOTEL \nO VALOR DE R$ {cobrados2:.2f}', file=cartao)
print('',file=cartao)
print(f'CARTÕES COBRADOS {dia}'.center(30), file=cartao)
print('-'*30, file=cartao)
print(f'{cabacalho:.<5}', end='', file=cartao)
print(f'{cabacalho2:.>15}', file=cartao)
for pos in range(0, len(apto)):
    if pos % 2 == 0:
        print(f'{apto[pos]:.<15}', end='', file=cartao)
    else:
        print(f'{apto[pos]:>5}', file=cartao)
print('', file=cartao)
cartao.close()
