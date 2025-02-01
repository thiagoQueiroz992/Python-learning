#EXERCÍCIO 065: Crie um programa que leia vários números inteiros. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar a digitar ou não.

n = 0
s = 0
answer = 's'
all_numbers = []

while answer in 'Ss':
    if answer in 'Ss' or answer in 'Nn':
        answer = 'S'
        n = int(input('Digite um número: '))
        answer = str(input('Quer continuar (S/N)? ')).strip()
        all_numbers.append(n)
        s += n
    else:
        print('Entrada inválida!')
med = s / len(all_numbers)
all_numbers.sort()
print(f'A média entre todos os números digitados foi {med:.1f}.')
print(f'O maior valor digitado foi {all_numbers[len(all_numbers) - 1]} e o menor foi {all_numbers[0]}.')
