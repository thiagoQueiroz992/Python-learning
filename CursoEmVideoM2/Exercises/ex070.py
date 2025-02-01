"""EXERCÍCIO 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    - Qual foi o total gasto na compra.
    - Quantos produtos custaram mais de R$ 1000
    - Qual é o nome do produto mais barato."""

#name = 'null'
price = higher_1000 = count = total = less_expensive_price = 0
less_expensive_name = 'null'
while True:
    print(f'\nPRODUTO {count + 1}:\n')
    name = str(input('Nome do produto: ')).strip().title()
    price = float(input('Preço do produto: R$'))
    cont = 'null'
    while cont not in 'SsNn':
        cont = str(input('Quer continuar [S/N]? ')).strip()[0]
    count += 1
    total += price
    if price > 1000: higher_1000 += 1
    if count == 1 or price < less_expensive_price:
        less_expensive_name = name
        less_expensive_price = price
    if cont in 'Nn': break
print(f'Nessa compra de {count} produto(s), o total foi de R${total:.2f}.')
print(f'{higher_1000} produtos custaram mais de R$1000.00.')
print(f'O produto mais barato foi {less_expensive_name}.')
