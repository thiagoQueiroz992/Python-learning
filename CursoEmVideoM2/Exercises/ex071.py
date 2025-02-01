value = int(input('Quanto você quer sacar? R$'))
n50 = value // 50
n20 = (value - n50 * 50) // 20
n10 = ((value - n50 * 50) - n20 * 20) // 10
n1  = (((value - n50 * 50) - n20 * 20) - n10 * 10) // 1

print('Você receberá, nesse saque:')
if n50 != 0: print(f'{n50} cédulas de R$50.00.')
if n20 != 0: print(f'{n20} cédulas de R$20.00.')
if n10 != 0: print(f'{n10} cédulas de R$10.00.')
if n1  != 0: print(f'{n1} cédulas de R$1.00')