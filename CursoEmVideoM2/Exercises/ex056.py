"""EXERCÍCIO 056: Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final do programa, mostre:
    - A média da idade do grupo
    - Qual é o nome do homem mais velho
    - Quantas mulheres tem menos de 20 anos"""

older_man = 'null'
older_man_age = 0

women_less_20 = 0

ages = []

for c in range(0, 4):
    print(f'PESSOA {c + 1}:')
    name = str(input('Qual é o seu nome? '))
    age = int(input('Qual é a sua idade? '))
    ages.append(age)
    sex = int(input('''Qual é o seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino\n'''))
    print('Masculino' if sex == 1 else 'Feminino')
    print('-' * 45)
    
    if sex == 1:
        if c == 0:
            older_man = name
            older_man_age = age
        else:
            if age > older_man_age:
                older_man = name
                older_man_age = age
                
    if sex == 2 and age < 20:
        women_less_20 += 1

#Calculando a média das idades
med_age = (ages[0] + ages[1] + ages[2] + ages[3]) / (len(ages))
print(f'A média das idades dessas pessoas é de {med_age} anos.')

#Exibindo o homem mais velho
print(f'O homem mais velho é {older_man}, que tem a idade de {older_man_age} anos.')

#Exibindo a quantidade de mulheres com menos de 20 anos
print(f'{women_less_20} dessas mulheres tem menos de 20 anos.')