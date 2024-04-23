frase = 'O python é uma linguagem de programação' 


i = 0
qtd_frequencia = 0
letra_mais_frequente = ''

while i < len (frase):
    letra = frase[i]
    
    if letra == ' ':
        i += 1
        continue
    
    vezes_letra_apareceu = frase.count(letra)
    
    if qtd_frequencia < vezes_letra_apareceu:
        qtd_frequencia = vezes_letra_apareceu
        letra_mais_frequente = letra
        
    print (f"A letra mais frequente é '{letra}', que apareceu {vezes_letra_apareceu} vezes.")
