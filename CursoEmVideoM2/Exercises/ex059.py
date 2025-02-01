"""EXERCÍCIO 059: Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

choice = 4
value_a = 0
value_b = 0
answer = 0
greater = []
while choice != 5:
    if choice == 1:
        answer = value_a + value_b
        print(f'A soma entre {value_a} e {value_b} é {answer}.')
        choice = 5
    elif choice == 2:
        answer = value_a * value_b
        print(f'O produto entre {value_a} e {value_b} é {answer}.')
        choice = 5
    elif choice == 3:
        greater = [value_a, value_b]
        greater.sort()
        answer = greater[1]
        print(f'O maior valor é {answer}.')
        choice = 5
    else:
        value_a = int(input('Digite um primeiro valor: '))
        value_b = int(input('Digite um segundo valor: '))
        choice = int(input('''Agora escolha:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\n'''))
