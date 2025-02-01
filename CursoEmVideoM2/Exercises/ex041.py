"""EXERCÍCIO 041: A Confederação Nacional de Natação (ConfNN) precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
    - Até 9 anos (mirim)
    - Até 14 anos (infantil)
    - Até 19 anos (júnior)
    - Até 20 anos (sênior)
    - Acima (master)"""

from datetime import date
from time import sleep

print('\033[1;33m=' * 40)
print('==========CATEGORIA DE NATAÇÃO==========')
print('=' * 40 + '\033[m')

b_year = int(input('Em qual ano você nasceu? '))
c_year = date.today().year

if b_year > date.today().year:
    print('Esse ano é inválido. Por favor seja sincero.')
else:
    age = c_year - b_year
    print('\033[1;36mPROCESSANDO OS DADOS. AGUARDE...\033[m')
    sleep(2.5)
    
    if age > 20:
        print('Sua categoria será: \033[32mMASTER.')
    elif age > 19:
        print('Sua categoria será: \033[32mSENIOR.')
    elif age > 14:
        print('Sua categoria será: \033[32mJUNIOR.')
    elif age > 9:
        print('Sua categoria será: \033[32mINFANTIL.')
    else:
        print('Sua categoria será: \033[32mMIRIM.')
