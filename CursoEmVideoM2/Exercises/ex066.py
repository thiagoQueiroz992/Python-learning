#EXERCÍCIO 066: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = s =  0
while True:
    n = int(input('Digite um número (Digite 999 se quiser que pare): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores exibidos foi de {s}.')