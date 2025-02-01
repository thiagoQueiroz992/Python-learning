#EXERCÍCIO 045: Crie um programa que faça o computador jogar Jokenpô com você!

from random import randint
from time import sleep

print('''\033[1;33mVocê e o computador jogarão pedra, papel e tesoura.
Primeiro você escolhe, depois ele vai escolher.
O computador não saberá o que você escolheu até que ele também revele o que ele escolheu.
Estão prontos?\033[m''')
sleep(3)
print('')
player_choose = str(input('Escolha um, pedra, papel ou tesoura: '))
player_choose = player_choose.strip()
player_choose = player_choose.upper()

print(f'Você escolheu: {player_choose}.')
sleep(1)

print('\033[1;34m\n'
      'COMPUTADOR:\033[m Agora é a minha vez!')
sleep(1.5)
print('\033[1;36mESCOLHENDO...\033[m')
sleep(4)
pc_choose = randint(0, 2)
print('Pronto, escolhi! Vamos continuar?\n')
input('Pressione enter para continuar')
sleep(1)
print('JOOOOO')
sleep(0.5)
print('KEEEEN')
sleep(0.5)
print('POOOOO')
sleep(1.5)

pc_c_str = None

if pc_choose == 0:
    pc_c_str = 'PEDRA'
elif pc_choose == 1:
    pc_c_str = 'PAPEL'
else:
    pc_c_str = 'TESOURA'

print(f'Você escolheu {player_choose}.')
print(f'O computador escolheu {pc_c_str}.')

sleep(1)

if player_choose == pc_c_str:
    print('\n\033[1;34mCOMPUTADOR:\033[m Deu empate! Jogamos muito bem!')
elif (player_choose == 'PEDRA' and pc_c_str == 'PAPEL') or (player_choose == 'PAPEL' and pc_c_str == 'TESOURA') or (player_choose == 'TESOURA' and pc_c_str == 'PEDRA'):
    print('\n\033[1;34mCOMPUTADOR:\033[m Haha, ganhei de você!')
else:
    print('\n\033[1;34mCOMPUTADOR:\033[m Você ganhou de mim, parabéns!')