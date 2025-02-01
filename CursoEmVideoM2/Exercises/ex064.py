#EXERCÍCIO 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

s = 0
count = -1
n = 0
while n != 999:
    s += n
    count += 1
    n = int(input('Digite um número: [999 para parar] '))
print(f'Foram digitados {count} número(s) até 999 ser digitado.')
print(f'A soma desses números digitados foi {s}.')