#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%Y %Hh%Mmin')
print(hora)
eventos= {'Coca-cola': 6.90, 'Guaraná' }
print(eventos.items())



