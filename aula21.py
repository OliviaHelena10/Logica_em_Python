# concatenando e extendendo listas 
# append -> adiciona um item ao final da lista
# insert -> adiciona um item no índice escolhido
# pop -> remove um item do final ou no índice escolhido
# del -> apaga um índice
# clear -> limpa a lista 
# extend -> extende a lista
# + - concatena listas

lista_a = [1, 2, 3, 4]
lista_b = [4, 5, 6, 7]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print (lista_d)
print (lista_a)