#EXERCÍCIO 033: Faça um programa que leia 3 números e diga qual deles é o maior e qual deles é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

n_conj = [n1, n2, n3]
n_conj.sort()

print(f'O maior desses números é {n_conj[2]} e o menor deles é {n_conj[0]}.')