"""EXERCÍCIO 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o computador deve perguntar se o usuário quer continuar ou não. No final, mostre
    - Quantas pessoas tem mais de 18 anos.
    - Quantos homens foram cadastrados.
    - Quantas mulheres tem menos de 20 anos."""

age = higher_18 = men = less_20_women = cadastred = 0
sex = 'null'
while True:
    print('=' * 30)
    print('CADASTRE UMA PESSOA')
    print('=' * 30 + '\n')
    age = int(input('IDADE: '))
    sex = 'null'
    while sex not in 'MmFf':
        sex = str(input('SEXO [M/F]: ')).strip()[0]
        #continue
    cont = str(input('Deseja continuar [S/N]? ')).strip()[0]
    cadastred += 1
    if age > 18: higher_18 += 1
    if sex in 'Mm': men += 1
    if sex in 'Ff' and age < 20: less_20_women += 1
    if cont in 'Nn': break
print(f'Das {cadastred} pessoas cadastradas, {higher_18} tem mais de 18 anos, {men} são homens e {less_20_women} são mulheres com menos de 20 anos.')
    