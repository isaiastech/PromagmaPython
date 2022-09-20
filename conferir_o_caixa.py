#!/usr/bin/python
# -*- coding: UTF-8 -*-

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


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" NÃO É VALIDO!!\033[m')
        else:
            valido = True
            return float(entrada)


def contador(*num):
    cont = 0
    cont2 = 1
    while True:
        valor = float(input(f'{cont2}º valor? ').replace(',', '.'))
        cont2 += 1
        if valor == 0:
            break
        cont += valor
    return cont


def lin():
    print('-'*60)
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

#COMECEI USAR O PROGRAMA EM 01/09/2019.
#COMECEI A USAR O ARQUIVO TXT EM 23/05/2020

from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%Y %Hh%Mmin')
arquivo = open('Caixa.txt', 'a', encoding="utf-8")
lin()
vermelho(f'\t\t\tCAIXA DO DIA {hora}\033[m')
lin()
verde('PARA FINALIZAR MOEDAS EMBALADAS>>00\033[m'.center(60))
lin()
cont = 1
pct = totpct = 0
while True:
    pct = leiaDinheiro(f'\033[1;35m{cont}º Moedas embaladas R$: ')
    cont += 1
    if pct == 0:
        break
    totpct += pct
m1 = leiaInt('\033[1;35mMoedas de R$ 1.00 : ')
sm1 = (m1 * 1)
m50 = leiaDinheiro('Moedas de R$ 0.50 : ' )
sm50 = (m50 * 0.50)
m25 = leiaDinheiro('Moedas de R$ 0.25 : ')
sm25 = (m25 * 0.25)
m10 = leiaDinheiro('Moedas de R$ 0.10 : ')
sm10 = (m10 * 0.10)
m05 = leiaDinheiro('Moedas de R$ 0.05 : \033[m')
sm05 = (m05 * 0.05)

#Soma das Moedas

totmoedas= (sm1 + sm50 + sm25 + sm10 + sm05 + totpct)

#TOTAL DE MOEDAS

verde(f'O total de moedas é R${totmoedas:.2f}\033[m')
lin()
d50 = leiaDinheiro('\033[1;92mNotas de R$ 50.00 : ')
sd50 = (d50 * 50)
d20 = leiaDinheiro('Notas de R$ 20.00 : ')
sd20 = (d20 * 20)
d10 = leiaDinheiro('Notas de R$ 10.00 : ')
sd10 = (d10 * 10)
d5 = leiaDinheiro('Notas de R$ 5.00 :  ')
sd5 = (d5 * 5)
d2 = leiaDinheiro('Notas de R$ 2.00 :  ')
sd2 = (d2 * 2)
totaldinh = (sd50 + sd20 + sd10 + sd5 + sd2)
azul(f'O total de dinheiro R$ {totaldinh :.2f}\033[m')
lin()
cont=1
vales = totvales = 0
while True:
        vales = leiaDinheiro(f'\033[1;35m{cont}º Vales no Caixas >>FINALIZAR >00>> R$ : ') #TOTAL DE VALES
        cont +=1
        if vales== 00:
           break
        totvales += vales
amarelo(f'O total de vales é R$ {totvales:.2f}\033[m')
lin()
cont=1
cartao = totalcard = 0
while True:
    cartao = leiaDinheiro(f'\033[1;34m{cont}º Cartões de Crédito (FINALIZAR>00)R$ : ') #TOTAL DE CARTÃO
    cont +=1
    if cartao == 0:
        break
    totalcard += cartao
amarelo(f'O total de Cartões é R$ {totalcard :.2f}\033[m')
lin()

#TOTAL DO CAIXA

Somatotalcaixa = (totmoedas )+ (totaldinh) + (totvales) + (totalcard) - (500)
caixa = leiaDinheiro('\033[1;92mDigite o valor a ser descontado em dinheiro R$ ')
caixa2= leiaDinheiro('Digite o Valor a ser descontado em cartão R$ ')
cheque= leiaDinheiro('Digite o valor em cheques R$ ')
somacaixa = (caixa + caixa2 + cheque)
totalgeral = Somatotalcaixa - somacaixa
lin()
print(f'\033[1;32m A soma total do caixa é R$ {Somatotalcaixa :.2f} menos R$ {somacaixa :.2f}\ne sobrou R$ {totalgeral :.2f}')
lin()
if totalgeral < 0:
    vermelho(f'O CAIXA ESTÁ FALTANDO R$ {totalgeral :.2f}\033[m')
elif totalgeral == 0:
    azul('O CAIXA ESTÁ CORRETO NÃO SOBROU NADA !!!\033[m')
elif totalgeral > 0:
    azul(f'O CAIXA ESTÁ SOBRANDO R$ {totalgeral :.2f}\033[m')
print(f'    RESUMO DO CAIXA {hora}\n'
      '--------------------------------------------------\n'
      f"O total de moedas    R${totmoedas:.2f}\n"
      f"O total de dinheiro  R${totaldinh :.2f}\n"
      f"O total de vales     R${totvales:.2f}\n"
      f'O total de Cartões   R${totalcard :.2f}\n'
      '---------------------------------------------------\n'
      f'O total a ser descontado do caixa é R${somacaixa:.2f}\n'
      f'O total do caixa {Somatotalcaixa + 500:.2f} menos o fundo de caixa (R$500,00)\nSobra R${totalgeral:.2f}\n'
      '----------------------------------------------------\n', file=arquivo)
arquivo.close()
