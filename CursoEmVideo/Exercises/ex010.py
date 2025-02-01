#EXERCÍCIO 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
#ela pode comprar
#DÓLAR: R$ 6,1
#EURO: R$ 6,41
#IENE: R$ 0,04

money = float(input('Quanto dinheiro você tem? R$ '))
dollar = money / 6.1
euro = money / 6.41
yen = money / 0.04

print(f'Com R$ {money:.2f} você pode comprar US$ {dollar:.2f};')
print(f'você pode comprar {euro:.2f}EUR')
print(f'e você pode comprar ¥{yen:.2f}')