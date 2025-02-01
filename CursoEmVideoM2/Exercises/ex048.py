#EXERCÍCIO 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

s = 0
ct = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        ct += 1
print(f'A soma de todos os {ct} valores solicitados é {s}')