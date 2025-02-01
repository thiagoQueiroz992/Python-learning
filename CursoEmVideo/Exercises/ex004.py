#EXERCÍCIO 004: Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as
#informações possíveis sobre ele.

thing = input('Digite algo: ')

print(f'Seu tipo primitivo é: {type(thing)}.')
print(f'É alfanumérico? {thing.isalnum()}.')
print(f'É alfa? {thing.isalpha()}.')
print(f'Está isento de acentos? {thing.isascii()}.')
print(f'É um dígito? {thing.isdigit()}.')
print(f'Está apenas em minúsculas? {thing.islower()}.')
print(f'É um valor decimal? {thing.isdecimal()}.')
print(f'É um identificador? {thing.isidentifier()}.')
print(f'É numérico? {thing.isnumeric()}.')
print(f'Pode ser impresso? {thing.isprintable()}.')
print(f'São apenas espaços? {thing.isspace()}.')
print(f'Está capitalizado? {thing.istitle()}.')
print(f'Está apenas em maiúscula? {thing.isupper()}.')