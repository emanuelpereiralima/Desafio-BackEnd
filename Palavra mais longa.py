'''
Palavra mais longa
Escreva uma função, que receba uma String e retorne a palavra mais longa desta String.

Se houver duas ou mais palavras com o mesmo comprimento, retorne a primeira palavra mais longa da String.
Ignore as pontuações e a situação em que a String será vazia.
As palavras também podem conter números, mas somente as letras serão consideradas no tamanho da palavra.
'''

entrada = input().split()
saida = ""

for x in entrada:
  #verifica se o tamanho da nova string é maior que a ja armazenada 
  if len(x) > len(saida):
    # verifica se não contém números junto das palavras
    if x.isalpha() == True:
      saida = x

print(saida)