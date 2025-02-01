#EXERCÍCIO 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15%
#de aumento

salario_inicial = float(input('Quanto é o salário do funcionário? R$'))
salario_reajuste = salario_inicial + (salario_inicial * 15 / 100)

print(f'O funcionário que recebia R${salario_inicial:.2f}, com o aumento de 15%,\npassará a receber R${salario_reajuste:.2f}.')