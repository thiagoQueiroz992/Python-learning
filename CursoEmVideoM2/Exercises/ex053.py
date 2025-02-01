#EXERCÍCIO 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo*, desconsiderando os espaços.
#*Palíndromo - frases que podem ser lidas de frente pra trás ou de trás pra frente que dá no mesmo.

phrase = str(input('Digite uma frase: '))
phrase_united = phrase.replace(' ', '')
phrase_united = phrase_united.lower()

phrase_list_crescent = []
phrase_list_decrescent = []

for c in range(1, len(phrase_united) + 1):
    phrase_list_crescent.append(phrase_united[c - 1])
for c in range(len(phrase_united), 0, -1):
    phrase_list_decrescent.append(phrase_united[c - 1])

if phrase_list_crescent == phrase_list_decrescent:
    print(f'A frase "{phrase}" é um palíndromo.')
else:
    print(f'A frase "{phrase}" não é um palíndromo.')