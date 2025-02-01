"""EXERCÍCIO 019: Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa
   que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome escolhido"""

from random import choice

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

choosed = choice([a1, a2, a3, a4])
print(f'O aluno escolhido foi {choosed}.')