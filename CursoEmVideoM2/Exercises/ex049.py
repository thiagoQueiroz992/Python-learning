#EXERCÍCIO 049: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

n = int(input('Digite um número para ver sua tabuada: '))

print(f'Segue abaixo a tabuada do número {n}:')
print('-' * 20)
for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')
print('-' * 20)