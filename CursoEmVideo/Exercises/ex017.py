#EXERCÍCIO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
#triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))

#h = sqrt(pow(ca, 2) + pow(co, 2))
h = hypot(ca, co)

print(f'Com os catetos de comprimento {ca:.1f} e {co:.1f}, a hipotenusa vai medir {h:.1f}')