
"""

# split, join e strip são métodos muito úteis da str
# Lista de listas e seus índices

"""


# split, join e strip são métodos muito úteis da str

    # split --> divide uma string (rslit = tira da direita) (lslipt = tira da esquerda)
    # join --> une uma string


frase = ' Olha que coisa mais linda,,  mais cheia de graça,,  é ela a menina que vem e que passa,,  num doce balanço a caminho do mar.'
lista_palavras = frase.split(', ') # separa pelo parâmetro (vírgula)
# lista_palavras = frase.split('') --> separa pelos espaços
# print ( lista_palavras )


for indice in lista_palavras:
    print ( indice )
    

"""
outra_lista = []
for i, frase in enumerate( lista_palavras ):
    outra_lista.append( lista_palavras[i].strip() )
print ( lista_palavras )
print ( outra_lista )
"""

frases_unidas = ''.join( lista_palavras )
# o join só aceita valores iteráveis, ou seja strings, listas, tuplas
print (frases_unidas)



# Lista de listas e seus índices

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)