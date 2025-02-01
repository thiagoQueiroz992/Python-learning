#EXERCÍCIO 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

higher_18 = 0
less_18 = 0

for c in range(0, 7):
    year = int(input('Qual é o seu ano de nascimento? '))
    current = date.today().year
    if current - year < 21:
        less_18 += 1
    else:
        higher_18 += 1
print(f'Dessas 7 pessoas, {less_18} ainda é(são) menor(es) de idade e {higher_18} já é(são) maior(es) de idade.')