# while e break

"""
number = 10

number /= 2
print (number)
print ('Acabou.')
"""

# while + continue - pulando alguma repetição
contador = 0

while contador < 40:
    contador += 1
    
    if contador == 6:
        print ('pule')
        continue
    
    if contador >= 21 and contador <=40:
        continue
    
    print (contador)
#    if contador == 8:
#        break
print ('acabou')