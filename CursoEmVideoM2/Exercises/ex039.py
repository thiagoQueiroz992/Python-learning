"""EXERCÍCIO 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar
    - Se é a hora de ele se alistar
    - Se já passou do prazo de ele se alistar
    Seu programa também deverá mostrar o tempo que falta ou que já passou para o alistamento."""

from time import sleep
from datetime import date

print('\033[1;33m' + '-=-' * 20)
print('|VERIFICADOR DE ALISTAMENTO|')
print('-=-' * 20 + '\033[m')

year = int(input('Em qual ano você nasceu, meu jovem? '))
print('\033[1;36mPROCESSANDO OS DADOS. AGUARDE...\033[m')
sleep(3.5)

age = date.today().year - year

if age < 18:
    print(f'\033[32mVocê ainda se alistará no futuro. Faltam {18 - age} ano(s) pra chegar sua idade.')
elif age == 18:
    print('\033[33mAcorda! Tá na hora de se alistar!')
else:
    print(f'\033[31mJá passou da hora do alistamento. Você deve procurar urgentemente uma junta militar, pois você deveria ter se alistado a {age - 18} ano(s)!')