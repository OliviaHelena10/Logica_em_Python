# cuidado com dados mutáveis !
# (imutáveis) copiando o valor - nesse caso, se A muda, B NÃO muda
# (mutáveis) aponta para o mesmo valor na lista - nesse caso, se A muda, B tbm muda
lista_a = ['Olívia', 'Helena', 1, True]
# lista_b = lista_a # ----> mutável
lista_b = lista_a.copy () # ----> imutável

lista_a [2] = 'Lima'
print (lista_a)
print (lista_b)