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

#Programa principal
from datetime import datetime
data_atual = datetime.now()
data_em_texto = data_atual.strftime('%d-%m-%Y')
ano = data_atual.strftime("%Y")
print(ano)

#Código refatorado em 14/09/2022
#Lista com valores para o café

cafe = ["cafe", 55.00, "infantil", 27.50, "vinho", 10.90] #Valores dos produtos do café
print('-'*46)
print('\033[1;31mCAFÉ COLONIAL DIA V 2.0'.center(50))
print(f'{data_em_texto}\033[m'.center(50))
print('-'*46)
try:
    n1 = leiaInt(f'\033[1;32m Digite a Quantidade de cafés Uni. R$ {cafe[1]}0? ')
    n2 = leiaInt(f'\033[1;32m Quantidade de cafés infantil Uni R$ {cafe[3]}0? ')
    n3 = leiaInt(f'\033[1;32m Quantas taças de vinho Uni. R$ {cafe[5]}0 ? ')
except:
    print('Houve um erro na execução do programa :(')
try:
    outros = soma1 = 0
    while True:
        outros = leiaDinheiro('Mais alguma coisa (FINALIZAR..000>>)? ')
        if outros == 0:
            break
        soma1 += outros
except:
    print('\033[1;31mHouve um erro de digitação de Valor :(\033[m')
soma = (n1 * cafe[1]) + (n2 * cafe[3]) + (n3 * cafe[5]) + soma1
print(f'\033[1;31mO valor total da comanda é R$ {soma:.2f}\033[m')
valor = leiaDinheiro('Valor recebido: R$ ')
troco = (valor - soma)
print(f'\033[1;32m O valor do troco é R$ {troco:.2f}')
