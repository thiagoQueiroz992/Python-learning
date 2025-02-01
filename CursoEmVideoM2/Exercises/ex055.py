#EXERCÍCIO 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

heights = []
for c in range(0, 5):
    height = float(input('Qual o seu peso (em kg)? '))
    heights.append(height)
heights.sort()
print(f'O menor peso é {heights[0]}kg e o maior é {heights[len(heights) - 1]}kg.')