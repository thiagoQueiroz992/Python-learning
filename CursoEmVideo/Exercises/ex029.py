"""EXERCÍCIO 029: Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada km acima do limite."""

from time import sleep

car_speed = int(input('Qual a velocidade do carro (em km/h)? '))
print('PROCESSANDO...')
sleep(2)

if car_speed > 80:
    spd_h_lmt = car_speed - 80
    fine_price = spd_h_lmt * 7
    
    print(f'Você foi multado! Você atingiu a velocidade de {car_speed}km/h, e sua multa será de {fine_price} reais.')
    
else:
    print('Você dirigiu dentro dos limites.')