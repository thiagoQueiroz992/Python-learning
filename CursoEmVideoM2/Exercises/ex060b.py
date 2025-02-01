"""EXERCÍCIO 060: Faça um programa que leia qualquer número e mostre na tela seu fatorial.
    Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
    Use o loop for."""

n = int(input('Digite um número (v2): '))
factorial = factor = n
for factor in range(n, 1, -1):
    factorial *= (factor - 1)
print(f'O fatorial de {n}({n}!) é {factorial}.')