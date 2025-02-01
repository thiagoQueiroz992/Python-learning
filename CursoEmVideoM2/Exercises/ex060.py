"""EXERCÍCIO 060: Faça um programa que leia qualquer número e mostre na tela seu fatorial.
    Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input('Digite um número: '))
factorial = factor = n
while factor > 1:
    factorial *= (factor - 1)
    factor -= 1
print(f'O fatorial de {n} ({n}!) é {factorial}.')