#EXERCÍCIO 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

first_note = float(input('Primeira nota: '))
second_note = float(input('Segunda nota: '))

m = (first_note + second_note) / 2

print(f'A média entre {first_note:.1f} e {second_note:.1f} é {m:.1f}')