#EXERCÍCIO 061: Refaça o desafio 051, lendo o primeiro termo e a razaão da PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

n1 = int(input('Digite o primeiro termo da PA: '))
rate = int(input('Qual é a razão dessa PA? '))
terms_found = 1
terms = n1
print(f'Os 10 primeiros termos da PA de A¹ = {n1} e r = {rate} são:')
while terms_found <= 10:
    print(terms, end=' -> ')
    terms += rate
    terms_found += 1
print('FIM.')