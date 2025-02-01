#EXERCÍCIO 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

width = float(input('Largura da parede (em metros): '))
height = float(input('Altura da parede (em metros): '))

area = width * height
ink = area / 2

print(f'Sua parede tem a dimensão de {width}x{height}, e sua área é de {area}m².\nSerá(ão) necessário(s) {ink}l de tinta.')