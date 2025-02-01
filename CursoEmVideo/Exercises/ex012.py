#EXERCÍCIO 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

value = float(input('Digite um valor: R$'))
desconto = (value * 5) / 100

print(f'O valor que era de R${value:.2f}, aplicado o desconto de 5%, ficará valendo R${(value - desconto):.2f}.')