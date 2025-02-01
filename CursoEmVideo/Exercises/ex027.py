"""EXERCÍCIO 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

name = input('Qual o seu nome completo? ')

n_list = name.split()

print(f'''Primeiro nome: {n_list[0]}
Último nome: {n_list[n_list.__len__() - 1]}''')