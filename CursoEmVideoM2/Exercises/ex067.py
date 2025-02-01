#EXERCÍCIO 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um valor para ver sua tabuada: '))
    if n < 0: break
    print(f'Aqui está a tabuada do número {n}:')
    for c in range(0, 11):
        print(f'{n} x {c:2} = {n * c}')
print('Programa encerrado, já que essa tabuada não exibe resultados para números negativos.')