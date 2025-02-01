"""EXERCÍCIO 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
    - À vista (dinheiro / cheque / pix) - 10% de desconto.
    - À vista (cartão) - 5% de desconto.
    - Em até 2x no cartão - preço normal.
    - 3x ou mais no cartão - 20% de juros."""

from time import sleep

print('\033[1;32m=' * 65)
print('===============   CÁLCULO DE FORMA DE PAGAMENTO   ===============')
print('=' * 65 + '\033[m')

price = float(input('Qual o valor do produto? R$'))
payment = str(input('Você vai pagar à vista ou à prazo? '))
payment = payment.strip()
payment = payment.upper()

print('''\033[1;36m
PROCESSANDO SEUS DADOS. POR FAVOR AGUARDE ALGUNS INSTANTES...
\033[m''')
sleep(2)

if 'VISTA' in payment:
    new_payment = str(input('Você vai pagar com \033[34mdinheiro, cheque, pix ou cartão?\033[m '))
    new_payment = new_payment.strip()
    new_payment = new_payment.upper()

    print('''\033[1;36m
PROCESSANDO SEUS DADOS. POR FAVOR AGUARDE ALGUNS INSTANTES...
    \033[m''')
    sleep(2)
    
    if 'DINHEIRO' in new_payment or 'CHEQUE' in new_payment or 'PIX' in new_payment:
        price = price - 100 / price * 10
        print(f'Você terá \033[1m10% de desconto\033[m, e o valor do produto passará a ser de \033[32mR${price:.2f}\033[m.')
    elif 'CARTAO' in new_payment or 'CARTÃO' in new_payment:
        price = price - 100 / price * 5
        print(f'Você terá \033[1m5% de desconto\033[m, e o valor do produto passará a ser de \033[32mR${price:.2f}\033[m.')
    else:
        print('\033[31mEssa forma de pagamento não é válida.\033[m')
        
elif 'PRAZO' in payment:
    parcels = int(input('Você vai pagar de quantas vezes? '))

    print('''\033[1;36m
PROCESSANDO SEUS DADOS. POR FAVOR AGUARDE ALGUNS INSTANTES...
    \033[m''')
    sleep(2)
    
    if parcels <= 2:
        print(f'Você pagará o \033[1mpreço normal\033[m, sendo de \033[32m{parcels}x de R${(price / parcels):.2f}\033[m cada.')
    else:
        price = price + (price * 20 / 100)
        print(f'Você deverá pagar \033[1m20% de juros por mês\033[m, totalizando um gasto de \033[32mR${price:.2f}\033[m.')
    
else:
    print('\033[31mEssa forma de pagamento não é válida.\033[m')