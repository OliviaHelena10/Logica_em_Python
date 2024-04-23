# Tipo list - Introdução às listas mutáveis em Python
# Suporta valores de qualquer tipo
"""
    Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""



lista = [1.2, 'Olívia', True, 123]
#print( bool ([]) ) #falsy
#print (lista, type (lista))
lista[1] = 'Maria'
del lista[3]
print (lista[1])
lista.append(False)
lista.pop()
ultimo_item = lista.pop(0)
print (lista)
print (f'item removido: {ultimo_item}')