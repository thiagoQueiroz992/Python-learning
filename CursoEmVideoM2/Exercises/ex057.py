#EXERCÍCIO 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até vir um valor correto.

sex = 'null'
while sex != 'M' and sex != 'F':
    sex = str(input('Qual o seu sexo? ')).upper()
    if sex != 'M' and sex != 'F':
        print('Entrada inválida. Por favor digite novamente.')
print(f'O seu sexo é {sex}.')