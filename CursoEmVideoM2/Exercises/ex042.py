"""EXERCÍCIO 042: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - Equilátero (todos os lados iguais)
    - Isósceles (apenas dois lados iguais)
    - Escaleno (todos os lados diferentes)"""

from time import sleep

print('\033[1;33m=' * 45)
print('========  VERIFICADOR DE TRIÂNGULOS  ========')
print('=' * 45 + '\033[m')

a1 = float(input('Digite um primeiro valor: '))
a2 = float(input('Digite um segundo valor: '))
a3 = float(input('Digite um terceiro valor: '))

print('\033[1;36mPROCESSANDO OS DADOS. AGUARDE...\033[m')
sleep(2.5)

if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('\033[32mSerá possível sim formar um triângulo!\033[m')
    if a1 == a2 == a3:
        print('Esse triângulo será um triângulo \033[34mequilátero.\033[m')
    elif a1 != a2 != a3 != a1:
        print('Esse triângulo será um triângulo \033[34mescaleno.\033[m')
    else:
        print('Esse triângulo será um triângulo \033[34misósceles.\033[m')
        
else:
    print('\033[31mNão será possível formar um triângulo.\033[m')