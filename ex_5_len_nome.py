# Exercício guiado com while
nome = 'Olívia Helena'
tamanho = (len(nome))

indice = 0
new_nome = ''

while indice < tamanho:
    letra = (nome[indice])
    new_nome += f' ~ {letra}'
    indice += 1

print (new_nome)