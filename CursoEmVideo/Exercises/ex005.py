#EXERCÍCIO 005: Faça um programa que leia um número e mostre na tela seu antecessor e seu sucessor

print('-=-' * 20)
print('\033[1mAnalisando antecessores e sucessores\033[m')
print('-=-' * 20)
print('')

x = int(input('Digite um número: '))

print(f'Analisando o número \033[32m{x}\033[m, seu antecessor é \033[31m{x - 1}\033[m e seu sucessor é \033[36m{x + 1}\033[m.')