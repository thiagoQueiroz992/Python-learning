#EXERCÍCIO 035: Crie um programa que pegue o comprimento de três retas e diga se é possível ou não formar um triângulo com essas três retas.

r1 = float(input('Quanto mede a primeira reta? '))
r2 = float(input('Quanto mede a segunda reta? '))
r3 = float(input('Quanto mede a terceira reta? '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('É sim possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo.')