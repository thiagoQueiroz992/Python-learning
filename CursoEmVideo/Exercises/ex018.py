#EXERCÍCIO 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
#tangente.

import math

a = float(input('Digite o valor do ângulo que você deseja: '))

r = math.radians(a)
seno = math.sin(r)
cosseno = math.cos(r)
tangente = math.tan(r)

print(f'Analisando o ângulo de {a:.1f}°,\nSeu seno vale {seno:.2f},\nSeu cosseno vale {cosseno:.2f},\nSeu tangente vale {tangente:.2f}.')