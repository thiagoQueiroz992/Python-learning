#EXERCÍCIO 062: Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

n1 = int(input('Qual é o primeiro termo da PA? '))
rate = int(input('Qual é a razão dessa PA? '))
terms_found = 1
terms = n1
print(f'Os 10 primeiros termos da PA de A¹ = {n1} e r = {rate} são:')
while terms_found <= 10:
    print(terms, end=' -> ')
    terms += rate
    terms_found += 1
print('FIM.')
terms_found = 0

new_terms = 1

while new_terms != 0:
    new_terms = int(input('Deseja mostrar mais quantos termos? '))
    if new_terms != 0: print(f'Aqui estão mais {new_terms} termos dessa mesma PA:')
    while terms_found < new_terms:
        print(terms, end=' -> ')
        terms += rate
        terms_found += 1
    print('FIM')
    terms_found = 0
    
    
