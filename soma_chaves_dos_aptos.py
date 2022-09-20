# coding: iso-8859-1 -*-
from arquivos_recepcao.utilidades import cores
cont = 0
soma = 0
for cont in range(0, 6):
    caixa_cart = int(input(f'{cont+1}º caixa de Cartão: '))
    soma += caixa_cart
cart_casa = int(input('Total de Cartão com hospedes? '))
totalcart = (soma + cart_casa)
if totalcart == 300:
    cores.verde('Os cartões estão corretos não falta nada!!')
elif totalcart < 300:
    cores.vermelho(f'Está faltando {300 - totalcart} cartões!!')
else:
    cores.azul(f'Está sobrando {totalcart - 300} cartões.')
