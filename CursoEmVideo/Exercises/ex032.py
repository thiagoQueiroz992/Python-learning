#EXERCÍCIO 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

year = int(input('Digite um ano: '))
if year == 0: year = date.today().year

#print('Esse ano é bissexto.' if (year / 4).is_integer() == True year % 100 == 0 and year % 400 == 0 else 'Esse ano é solar.')
if year % 100 == 0 and year % 400 == 0:
    print(f'O ano de {year} é bissexto')
elif year % 4 == 0:
    print(f'O ano de {year} é bissexto')
else:
    print(f'O ano de {year} não é bissexto, mas sim solar.')