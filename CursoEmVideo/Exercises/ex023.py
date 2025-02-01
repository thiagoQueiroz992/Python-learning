#EXERCÍCIO 023: Faça um programa que leia um número entre 0 e 9999 e mostre na tela cada um dos seus dígitos separados.

number = input('Digite um valor qualquer entre 0 e 9999: ')

if number.isnumeric() and len(number) <= 4:
    un = 0
    dez = 0
    cen = 0
    unm = 0
    
    if len(number) >= 1:
        un = number[len(number) - 1]
    if len(number) >= 2:
        dez = number[len(number) - 2]
    if len(number) >= 3:
        cen = number[len(number) - 3]
    if len(number) == 4:
        unm = number[len(number) - 4]
    
    print(f'''Valor da unidade: {un}
Valor da dezena: {dez}
Valor da centena: {cen}
Valor da unidade de milhar: {unm}''')
else:
    print('Esse valor é inválido.')