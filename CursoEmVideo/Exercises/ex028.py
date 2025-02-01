#EXERCÍCIO 028: Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import  randrange
from time import sleep

desk_n = randrange(0, 6)
user_n = int(input('Estou pensando em um número, entre 0 e 5. Tenta adivinhar: '))
print('PROCESSANDO...')
sleep(2)
print(f'O número pensado foi {desk_n}.')
print('Parabéns, você acertou!' if user_n == desk_n else 'Que pena, você errou!')