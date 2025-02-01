#EXERCÍCIO 006: Crie um algoritmo que leia um número que mostre seu dobro, triplo e raiz quadrada

print('\033[1;36m-=-' * 20)
print('ANALISADOR DE DOBRO, TRIPLO E RAIZ QUADRADA')
print('-=-' * 20 + '\033[m')

n = int(input('\033[4mDigite um número:\033[m '))

colors = {'Green' : '\033[1;32m', 'Blue' : '\033[1;34m', 'Clear' : '\033[m'}

print(f'\033[3mConsiderando o número {colors['Green']}{n}{colors['Clear']}...\nSeu dobro é {colors['Blue']}{n * 2}{colors['Clear']}\nSeu triplo é {colors['Blue']}{n * 3}{colors['Clear']}\nSua raiz quadrada é {colors['Blue']}{(n ** (1/2)):.1f}{colors['Clear']}')