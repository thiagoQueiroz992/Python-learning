#EXERCÍCIO 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
primo = 0

for c in range(1, n):
    if n % c == 0:
        primo += 1
if primo == 1:
    print(f'O número {n} é primo.')
elif n <= 0:
    print('Não é possível descobrir se zero ou um número negativo é primo ou não')
elif primo == 0:
    print('O número 1 não é primo nem composto, pois ele é divisível apenas por si próprio.')
else:
    print(f'O número {n} não é primo, mas sim composto.')