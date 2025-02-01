"""EXERCÍCIO 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    - Abaixo de 18.5 (abaixo do peso)
    - Entre 18.5 e 25 (peso ideal)
    - 25 até 30 (sobrepeso)
    - 30 até 40 (obesidade)
    - Acima de 40 (obesidade mórbida)"""

from time import sleep

print('\033[1;33m=' * 40)
print('========   CALCULADORA DE IMC   ========')
print('=' * 40 + '\033[m')

height = float(input('Qual o seu peso (em kg)? '))
size = float(input('Qual a sua altura (em m)? '))

print('\033[1;36mPROCESSANDO OS DADOS. AGUARDE...\033[m')
sleep(2.5)

imc = height / (size ** 2)
print(f'O seu IMC é de \033[34m{imc:.1f}.\033[m')

if imc > 40:
    print('Você se encontra em uma situação de \033[31mobesidade mórbida.\033[m')
elif imc > 30:
    print('Você se encontra em uma situação de \033[31mobesidade.\033[m')
elif imc > 25:
    print('Você está com \033[33msobrepeso.\033[m')
elif imc > 18.5:
    print('Seu peso está na \033[32mmédia ideal.\033[m')
else:
    print('Você se encontra \033[33mabaixo do peso.\033[m')