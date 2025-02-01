#EXERCÍCIO 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
#porção inteira.

from math import trunc

n = float(input('Digite um valor: '))

print(f'O valor {n}, em sua porção inteira, fica {trunc(n)}')