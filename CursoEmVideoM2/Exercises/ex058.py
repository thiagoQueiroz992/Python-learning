#EXERCÍCIO 058: Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tryings = 0
desk_n = randint(0, 10)
player_n = int(input('Estou pensando em um número entre 0 e 10, tenta adivinhar: '))
tryings += 1
while player_n != desk_n:
    player_n = int(input('Você errou. Tente novamente: '))
    tryings += 1
print(f'Parabéns, você acertou! Você precisou de {tryings} tentativa(s) para acertar.')