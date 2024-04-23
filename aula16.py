string = 'Olívia Helena'

i = 0
while i < len(string):
    letra = string[i]

    print (letra)
    i += 1
    
    if letra == ' ':
        break

else:
    print ('Não encontrei um espaço na string')