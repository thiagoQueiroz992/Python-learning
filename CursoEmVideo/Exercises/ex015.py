#EXERCÍCIO 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00
#por dia e R$0,15 por km rodado.

km = float(input('Quantos quilômetros pecorreu? '))
days = int(input('Quantos dias foram gastos? '))

price = km * 0.15 + days * 60

print(f'Como você levou {days} dias e andou {km}km, seu gasto será de R${price:.2f}.')