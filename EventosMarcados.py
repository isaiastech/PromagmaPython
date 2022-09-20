from recepcao.arquivos_recepcao.utilidades.dataporextenco import dataextenso

eventos = []
while True:
    nome = str(input('Nome do Evento? ').upper())
    eventos.append(nome)
    res = str(input('Mais algum evento? S/N ').upper())
    if res == "N":
        break
    else:
        continue
print('--'*15)
print('Eventos do dia:')
print('')
for i in eventos:
    print(f' {i}')

print('--'*15)
salas = ['SALA ITAÚNA - SUB SOLO', 'SALA REAL - SUB SOLO', 'SALA BUSINESS - SUB SOLO','SALÃO JARAGUÁ - 7º ANDAR',
         'RESTAURANTE - TÉRREO', 'SALA DE TV - TÉRREO' ]
for salas in salas:
    print(salas)

print('--'*15)

dataextenso()

