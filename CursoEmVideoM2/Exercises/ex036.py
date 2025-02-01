"""EXERCÍCIO 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

from time import sleep

print('\033[1;33m-=-' * 20)
print('|APROVANDO EMPRÉSTIMOS|')
print('-=-' * 20 + '\033[m')

value = float(input('Qual o valor da casa? \033[3;34mR$\033[m'))
salary = float(input('Qual o seu salário? \033[3;34mR$\033[m'))
years = int(input('Em quantos anos você vai pagar? '))

months = years * 12
prest_value = value / months

salary_percentage = (prest_value / salary) * 100
print('\033[1;36mPROCESSANDO OS DADOS...\033[m')
sleep(3)

if salary_percentage <= 30:
    print(f'''\033[1;32mSeu empréstimo foi aprovado!\033[m
Você pagará R${prest_value:.2f} mensalmente por um período de {months} meses.''')
else:
    print(f'\033[1;31mSeu acesso foi negado, pois a prestação mensal é o equivalente a {salary_percentage}% de seu salário!')

