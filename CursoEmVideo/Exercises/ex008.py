#EXERCÍCIO 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

meters = int(input('Digite um valor em metros: '))

km = meters * 0.001
hm = meters * 0.01
dam = meters * 0.1
dm = meters * 10
cm = meters * 100
mm = meters * 1000

print(f'A medida de {meters:}m corresponde a:\n{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{dm}dm\n{cm}cm\n{mm}mm')