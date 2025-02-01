"""FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
   - Quantas vezes aparece a letra "A"
   - Em qual posição ela aparece pela primeira vez
   - Em qual posição ela aparece pela última vez"""

phrase = input('Escreva algo: ')

up = phrase.upper()
how_a = up.count('A')

start_a = up.find('A')
last_a = up.rfind('A')

print(how_a, start_a, last_a)