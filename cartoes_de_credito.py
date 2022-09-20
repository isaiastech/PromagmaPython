# coding: iso-8859-1 -*-
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

from datetime import date
data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%y')
print('--'*20)
print(f"    \033[1;31mCONFERE OS CARTÕES {data_em_texto}\033[m")
print("--" * 20)
cont=1
cartao=total=0
while True:
    cartao = leiaDinheiro(f'\033[1;32m{cont}º cartão (ENCERRAR >00)R$: ')
    cont +=1
    if cartao == 0:
        break
    total += cartao
print('=>'*30)
print(f'A soma total  de cartões é R$ {total:.2f}')
caixa = leiaDinheiro('\033[1;34mDigite o valor a ser descontado R$:')
total2=(total - caixa)
print('=>'*30)
print(f'\033[1;31mO valor a ser fechado no caixa é de R${total2:.2f}')
print('=>'*30)
if total2 ==0:
    print('\033[1;32mOS FECHAMENTOS DE CARTÃO ESTÃO OK')
elif total2 <0:
    print(f'\033[1;33mTEM FECHADO NO CAIXA O VALOR A MAIS DE R${total2:.2f}')
else:
    print(f'FALTA FECHAR O VALOR DE R${total2:.2f}')
