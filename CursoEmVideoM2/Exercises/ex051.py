#EXERCÍCIO 051: Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final, mostre os 10 primeiros termos dessa progressão

first_term = int(input('Qual o primeiro termo da PA? '))
pa_rate = int(input('Qual a razão dessa PA? '))

print(f'Os 10 primeiros termos da P.A. de A¹ = {first_term} e R = {pa_rate} são:')
print('-' * 20)
for c in range(first_term, first_term + 10 * pa_rate, pa_rate):
    print(c)
print('-' * 20)