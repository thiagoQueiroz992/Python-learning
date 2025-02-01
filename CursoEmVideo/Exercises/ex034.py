"""EXERCÍCIO 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.
    Para salários superiores a R$1.250,00, calcule um aumento de 10%
    Para inferiores ou iguais o aumento será de 15%."""

salary = int(input('Qual o valor de seu salário? R$'))

bonus = None

if salary > 1250:
    bonus = 10
else:
    bonus = 15
    
new_salary = salary + ((salary * bonus) / 100)
print(f'Com o aumento, seu salário passa a ser de R${new_salary:.2f}')