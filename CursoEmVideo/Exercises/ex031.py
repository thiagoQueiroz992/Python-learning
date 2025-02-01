"""EXERCÍCIO 031: Crie um programa que pergunte a distância de uma viagem em km.
    Calcule o preço da passagem, cobrando:
    R$0,50 para viagens com distância de até 200km
    R$0,45 para viagens de mais de 200km"""

from time import sleep

dist = int(input('Qual a distância de sua viagem (em km)? '))

ticket = dist * 0.50 if dist <= 200 else dist * 0.45
print('PROCESSANDO...')
sleep(2)

"""if dist <= 200:
    ticket = 0.50
else:
    ticket= 0.45"""


print(f'O valor da passagem será de {ticket:.2f} reais.')