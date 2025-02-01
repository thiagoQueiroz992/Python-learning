#EXERCÍCIO 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta
#para graus Fahrenheit.

celsius = float(input('Digite uma temperatura em °C: '))
fahrenheit = celsius * 1.8 + 32

print(f'A temperatura {celsius:.1f} °C corresponde a {fahrenheit:.1f} °F.')