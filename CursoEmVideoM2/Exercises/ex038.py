"""EXERCÍCIO 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das seguintes mensagens:
    - O primeiro valor é maior
    - O segundo valor é maior
    - Não existe valor maior, os dois são iguais"""

from time import sleep

print('\033[1;33m' + '-=-' * 20)
print('|COMPARADOR DE VALORES|')
print('-=-' * 20 + '\033[m')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('\033[1;36mPROCESSANDO OS DADOS, AGUARDE...\033[m')
sleep(3.5)

if n1 > n2:
    print('O \033[34mprimeiro valor\033[m é o maior.')
elif n2 > n1:
    print('O \033[34msegundo valor\033[m é o maior.')
else:
    print('Não existe valor maior, os dois são \033[34miguais\033[m.')