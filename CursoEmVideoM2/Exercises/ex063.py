"""EXERCÍCIO 063: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
    Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8..."""

n = int(input('Quantos elementos terá essa sequência de Fibonacci? '))
cont = 3
past = 0
seq = 1
next = 1
print(f'Segue abaixo uma sequência de Fibonacci com {n} elementos.')
while cont <= n:
    if cont == 3:
        print(past, end=' - ')
        print(seq, end=' - ')
        print(next, end=' - ')
    else:
        past = seq
        seq = next
        next = seq + past
        print(next, end=' - ')
    cont += 1
print('FIM.')