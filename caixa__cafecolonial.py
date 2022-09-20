# coding=UTF-8
# coding: iso-8859-1 -*-
def lin():
    print('~'*62)
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




#Progama principal

from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%y ')
lin()
print(f'FECHAMENTO DAS COMANDAS DO CAFÉ COLONIAL EM {hora}')
print('PARA FECHAR O PROGRAMA DIGITE 999')
lin()
caixa_cafe = open('caixa_cafe.txt', 'w', encoding="utf-8")
comandanum = []
valor = []
comanda = 0
total = 0
while True:
    numero = leiaInt('\033[1;34mCOMANDA Nº: ')
    comanda = leiaDinheiro('VALOR DA COMANDA R$ ')
    comandanum.append(numero)
    comandanum.append(comanda)
    if comanda == 999:
        break
    total +=comanda
lin()
print(f'O VALOR TOTAL DOS CAFÉS É R$ {total :.2f}')
print('-'*48, file=caixa_cafe)
print(f'Café Colonial {hora}'.center(50), file=caixa_cafe)
print('-'*48, file=caixa_cafe)
for pos in range(0, len(comandanum)):
    if pos % 2 == 0:
        print(f'Comanda Nº{comandanum[pos]:.<20}', end=' ', file=caixa_cafe)
    else:
        print(f'Valor R${comandanum[pos]:>7.2f}', file=caixa_cafe)
print('\n')
print('-'*48, file=caixa_cafe)
print(f'Total do Café R${total:.2f}'.center(50), file=caixa_cafe)
caixa_cafe.close()

