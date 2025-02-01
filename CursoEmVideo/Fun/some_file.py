phrase = 'Curso em Video Python'
sentencia = '   Aprenda Python  '

#FATIAMENTO
print(phrase[9]) #Apenas o caractere de índice 9 (V)
print(phrase[9:14]) #Os caracteres de 9 a 14, contando o 9 mas excluindo o 14 (Video)
print(phrase[9:21:2]) #Serão mostrados os caracteres no intervalo, pulando de 2 em 2 (VdoPto)
print(phrase[:5]) #Apenas os 5 primeiros caracteres serão mostrados (Curso)
print(phrase[15:]) #Apenas os caracteres a partir do 15 (incluindo ele) serão mostrados (Python)
print(phrase[9::3]) #Apenas os caracteres a partir do 9 (incluindo) serão mostrados, pulando de 3 em 3 (VePh)

print('=' * 20)

#ANÁLISE
ex1 = len(phrase) #Mostra o tamanho (em índices) da string (21)
print(ex1)

ex2 = phrase.count('o') #Mostra a quantidade de um determinado caractere que há na string ('o' possui 3)
print(ex2)

ex3 = phrase.count('o', 0, 13) #Mostra a quantidade de um determinado caractere, no intervalo dado ('o' = 1)
print(ex3)

ex4 = phrase.find('deo') #Mostra em qual índice começou a parte dada (Encontrou 'deo' começando no índice 11)
print(ex4)

ex5 = phrase.find('Android') #Se a string não tiver o valor dado, o retorno será (-1)
print(ex5)

ex6 = 'Curso' in phrase #Mostra se a string dada existe dentro da outra string (True)
print(ex6)

print('=' * 20)

#TRANSFORMAÇÃO
ez1 = phrase.replace('Python', 'Android') #Substitui a parte existente da string por outra que foi dada ('Curso em Video Android')
print(ez1)

ez2 = phrase.upper() #Transforma todas as letras em maiúsculas (CURSO EM VIDEO PYTHON)
print(ez2)

ez3 = phrase.lower() #Transforma todas as letras em minúsculas (curso em video python)
print(ez3)

ez4 = phrase.capitalize() #Deixa apenas a primeira letra maiúscula e todas as outras minúsculas (Curso em video python)
print(ez4)

ez5 = phrase.title() #Deixa apenas as letras após espaços maiúsculas (Curso Em Video Python)
print(ez5)

ez6 = sentencia.strip() #Remove todos os espaços que não possuem caracteres antes ou depois (Aprenda Python)
print(ez6)

ez7 = sentencia.rstrip() #Remove apenas os espaços que não possuem caracteres a direita, ou seja, os espaços da direita ('   Aprenda Python')
print(ez7 + '.')

ez8 = sentencia.lstrip() #Remove apenas os espaços que não possuem caracteres a esquerda, ou seja, os da esquerda ('Aprenda Python  ')
print(ez8 + '.')

print('=' * 20)

#DIVISÃO
es1 = phrase.split() #Divide a 'string' com espaços entre caracteres, cada uma como uma nova variável, e uma nova indexação, dentro de uma lista ('Curso', 'em', 'Video', 'Python')
print(es1)

#JUNÇÃO
es2 = '-'.join(es1) #Junta uma lista de 'strings', usando outra 'string' pra separar as palavras, nesse caso '-' (Curso-em-Video-Python)
print(es2)

print("""
=================
""")

#NADA A VER
#O uso de três aspas simples ou duplas como identificador de string permite que você faça quebras de linha dentro do código que também serão consideradas na função print.
print('''Olá,
Esta é uma carta,
Ou um poema,
Não faço a mínima ideia.
Autor desconhecido.''')

print('=' * 20)

#Também é possível usar duas funções ao mesmo tempo
print(phrase.count('O')) #0, pois todos os 'o's são minúsculos
print(phrase.upper().count('O')) #3, pois será primeiramente convertido em maiúsculas e assim o 'O' maiúsculo passará a existir.