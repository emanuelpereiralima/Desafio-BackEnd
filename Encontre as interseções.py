'''
Encontre as interseções
Escreva uma função, que receba um parâmetro de uma lista de String contendo dois elementos. Cada elemento contém uma string com sequência de números ordenados de forma crescente. E sua função deve retornar uma String contendo os números ordenados que aparecem nas duas listas: 
'''

import re
entrada = input().split('"')
temp = []
saida = ""
for x in entrada:
    if len(x) > 2:
        temp.append(re.findall('\d+', x))

for x in temp[0]:
    if x in temp[1]:
        saida += x + ","
        
print(saida[:-1])