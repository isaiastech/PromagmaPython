# coding: iso-8859-1 -*-
apto = str(input('Número do apto? '))
dia = int(input('Quantidades de diárias pagas? '))
fatura = str(input('Número da ficha razão? '))
gara = int(input('Quantidades de garagem? '))
nota = int(input('Número da nota fiscal? '))
if gara >=1 and nota >=1:
    print(f'O apto {apto} pagou {dia} Diária e {gara} garagem fatura: {fatura} e a nota fiscal número:{nota}'.upper())
elif gara >=1 and nota <1:
    print(f'O apto {apto} pagou {dia} Diária e {gara} garagem fatura: {fatura} e a nota fiscal não foi emitida.'.upper())
elif gara <1 and nota <1:
    print(f'O apto {apto} pagou {dia} diária com ficha razão:{fatura} e a nota fiscal não foi emitida.'.upper())
elif gara <1 and nota >1:
    print(f'O apto {apto} pagou {dia} diária com ficha razão:{fatura} e a nota fiscal número:{nota}'.upper())
