#EXERCÍCIO 068: Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 30)

from random import randint

n = count = 0
choice = 'null'

while True:
    n = int(input('Escolha um número, de 1 a 10: '))
    if 0 < n <= 10:
        choice = str(input('Agora escolha ímpar ou par [I / P]: ')).strip()[0]
        if choice in 'IiPp':
            print(f'O computador escolheu {'par' if choice in 'Ii' else 'ímpar'} e você escolheu {'ímpar' if choice in 'Ii' else 'par'}.')
            pc_choice = randint(1, 10)
            r = pc_choice + n
            print(f'{pc_choice} + {n} = {r}')
            ev_or_od = r % 2
            if (ev_or_od == 0 and choice in 'Pp') or (ev_or_od == 1 and choice in 'Ii'):
                print('O humano venceu!')
                count += 1
            else:
                print('O computador venceu!')
                break
        else:
            print('Escolha inválida.')
    else:
        print('Valor informado inválido.')
print(f'Você teve {count} {'vitória consecutiva' if count <= 1 else 'vitórias consecutivas'}.')
print('Fim de jogo!')