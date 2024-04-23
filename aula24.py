#  Introdução ao empacotamento e desempacotamento

# lista = ['Olívia', 'Joseane', 'Moisés', 'Victor']
# nome1, nome2, nome3, nome4 = lista
"""
_, nome2, *_ = ['Olívia', 'Joseane', 'Moisés', 'Victor']
print (nome2)
print (_)
"""


# tuplas
# a Tupla é imutável
nomes = ['Olívia', 'Joseane', 'Moisés', 'Victor']
nomes = tuple (nomes)
# nomes = list (nomes)
lista_enumerada = enumerate (nomes)
print (nomes[-1])
print (nomes)

for indice, nome in lista_enumerada:
    print(indice, nome)
    
# quando printamos a lista usando o for consumimos o iterador (enumerate) e não é
# mais possível imprimir novamente a lista pq ela está "vazia"
# para evitar isso, ao invés de usar uma variável eu posso usar o iterador
# quando for fazer o for:

# for nome in enumerate (nomes):
#     print (nomes)

# se eu precisar usar a lista novamente, ela ainda está disponível
