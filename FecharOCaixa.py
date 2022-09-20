# coding: iso-8859-1 -*-

def linhas():
    return print('-='*25)

def data():
    from datetime import datetime
    dia = datetime.now()
    datatex = dia.strftime('%d/%m/%Y %Hh%Mmin')
    return print(f'\033[1;32m{datatex}')

from datetime import date
def dataextenso():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    mes_ext = {1 : 'janeiro', 2 : 'fevereiro', 3 : 'mar�o', 4 : 'abril', 5 : 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
               9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    aniver = data_em_texto
    dia, mes, ano = aniver.split("/")
    print('%s de %s de %s' % (dia, mes_ext[int(mes)], ano))


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


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mVALOR INV�LIDO TENTE NOVAMENTE!!\33[m')
        if ok:
            break
    return valor


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" N�O � VALIDO!!\033[m')
        else:
            valido = True
            return float(entrada)


def contador(*num):
    cont = 0
    cont2 = 1
    while True:
        valor = float(input(f'{cont2}� valor? ').replace(',', '.'))
        cont2 += 1
        if valor == 0:
            break
        cont += valor
    return cont


def lin():
    print('-'*60)

def borda(s: str):
#C�digo copiado da aula de fun��es do  Prof. Me. Eng. Renan Portela Jorge.
    titulo = len(s)
    if titulo:
        print('+', '-' * titulo,'+')
        print('|', s, '|')
        print('+', '-' * titulo,'+')


from recepcao.arquivos_recepcao import utilidades
import textwrap
borda('VALORES A SEREM DESCONTADOS DO CAIXA V.1')


cont = 1
cart = totalcard = 0

vermelho('Para finalizar digite: 00'.center(40))
amarelo('')
while True:
    cart = leiaDinheiro(f'\33[1;34m{cont}� Cart�es de cr�dito(FINALIZAR 00): ')
    cont+=1
    if cart == 0:
        break
    totalcard += cart
print(f'Total de Cart�es R$ {totalcard:.2f}')
lin()
vermelho('    Para finalizar digite: 00')
vales = []
contarvales = val = 0
verde(' ')
while True:
    val = leiaDinheiro('VALOR EM VALES R$ ')
    vales.append(val)
    contarvales += 1
    if val == 00:
        break
    totaldevales = sum(vales)
print(f'Total de de Vales � R${sum(vales):.2f}')
lin()
vermelho('    Para finalizar digite: 00')
valorpix = []
contarpix = 0
amarelo('')
while True:
    pix = leiaDinheiro('VALOR EM PIX R$ ')
    valorpix.append(pix)
    contarpix += 1
    if pix == 0:
        break
    totalpix = sum(valorpix)

print(f'Total de PIX R${sum(valorpix):.2f}')
lin()
prazo = leiaDinheiro('Total em Dinheiro a ser descontado do caixa R$ ')
valorendinh = (prazo - sum(vales) - sum(valorpix) )
lin()
azul(f'O valor para mandar em dinheiro � R$ {valorendinh}\33[m')
print('')
print('')
#dinheiro = leiaDinheiro('Valor em dinheiro? R$ ')
#somarpix1 = valorpix
#somavales = vales
                                                         #Formata��o do texto para observa��es...
obs = str(input('Observa��o:\n'))
value = obs
wrapper = textwrap.TextWrapper(width=50)
word_list = wrapper.wrap(text=value)
#for element in word_list :
    #print(element)
                                                           #Soma geral somando vales , pix , cat�es...

somageral = (valorendinh + pix + totalcard + (sum(vales)))

print('')
print('')

borda(f'RESUMO DO CAIXA'.center(40))                       # Resumo do caixa
dataextenso()
print('')
print(f'VALOR EM DINHEIRO........R$ {valorendinh:.2f}')
print(f'VALOR EM PIX ............R$ {sum(valorpix):.2f}')
print(f'VALOR EM VALES...........R$ {sum(vales):.2f}')
print(f'VALOR EM CART�ES.........R$ {totalcard:.2f}')
lin()
print(f'Total Geral .............R$ {valorendinh + sum(valorpix) + totalcard + (sum(vales)):.2f}')
lin()
print('Observa��o: ')
for element in word_list :
    print(element)
lin()
