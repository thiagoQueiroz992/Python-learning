"""EXERCÍCIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
   - O nome com todas as letras maiúsculas
   - O nome com todas minúsculas
   - Quantas letras ao todo (Sem considerar espaços)
   - Quantas letras tem o primeiro nome"""

name = input('Qual o seu nome completo? ')

name_upper = name.upper()
name_lower = name.lower()
space_quant = name.count(' ')
name_wo_spaces = (len(name) - space_quant)
name_list = name.split()
first_name_letters = len(name_list[0])

print(f'''Nome em maiúsculas:
{name_upper}.

Nome em minúsculas:
{name_lower}.

Quantidade de letras total: {name_wo_spaces}.
Quantidade de letras (Primeiro nome): {first_name_letters}.''')
