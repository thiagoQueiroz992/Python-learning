#EXERCÍCIO 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

city = input('Me fale o nome de uma cidade: ')

city_new = city.strip()
c_nm_list = city.split()
print(f'A cidade {city_new} começa com a palavra "Santo"? {c_nm_list[0] == 'Santo'}')