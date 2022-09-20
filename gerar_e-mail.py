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

 # Programa principal
 #ultima modificação 14/08/2021
from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%y ')

lin()
print(hora)
nome = str(input('Digite o nome:')).strip().lower().replace(" ", "")
opção = leiaInt('''\033[1;32mEscolha um Servidor:
 [0]-@hotmail.br     [1]-@yahoo     [2]-@terra 
 [3]-@uol            [4]-@bol       [5]-@gmail  
 [6]-@icloud         [7]-outlook    [8]-outlook.br
 [9]hotmail.com
 =====>>>> : ''')
lin()
while True:
    if opção == 1:
        azul(f'{nome}@yahoo.com.br\033[m')
        break
    elif opção == 2:
        print(f'{nome}@terra.com.br\033[m')
        break
    elif opção == 3:
        azul(f'{nome}@uol.com.br\033[m')
        break
    elif opção == 4:
        azul(f'{nome}@bol.com.br\033[m')
        break
    elif opção == 5:
        azul(f'{nome}@gmail.com\033[m')
        break
    elif opção == 6:
        azul(f'{nome}@icloud.com\033[m')
        break
    elif opção == 0:
        azul(f'{nome}@hotmail.com.br\033[m')
        break
    elif opção == 7:
        azul(f'{nome}@outlook.com\033[m')
        break
    elif opção == 8:
        azul(f'{nome}@outlook.com.br\033[m')
        break
    elif opção == 9:
        azul(f'{nome}@hotmail.com\033[m')
        break
    else:
        vermelho('SERVIDOR INVÁLIDO !!\033[m')
        opção = leiaInt('\033[1;32mESCOLHA UM SERVIDOR VÁLIDO DE ( 0 à 9 ): ')

verde('''
BEM VINDOS !!

recepcao@hoteljaraguareal.com.br 

jaragua@hoteljaraguareal.com.br''')
