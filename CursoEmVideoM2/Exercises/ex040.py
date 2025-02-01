"""EXERCÍCIO 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de cordo com a média atingida:
    - Abaixo de 5.0 - Reprovado!
    - Entre 5.0 e 6.9 - Recuperação!
    - Acima de 7.0 - Aprovado!"""

from time import sleep

print('\033[1;33m=' * 40)
print('=============MÉDIA DE NOTAS=============')
print('=' * 40 + '\033[m')

n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))
print('\033[1;36mPROCESSANDO OS DADOS. AGUARDE...\033[m')

sleep(2.5)

med = (n1 + n2) / 2
print(f'Sua média foi \033[34m{med:.1f}.\033[m')

if med >= 7:
    print('\033[32mVocê foi aprovado! Parabéns!')
elif med >= 5:
    print('\033[33mVocê está de recuperação!')
else:
    print('\033[31mVocê foi reprovado!')