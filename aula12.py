"""
id - A identidade do valor que está na memória

flag -> marca um local
none = não valor
id vai mostrar o local onde está armazenado aquela variável

v1 = 'a'
v2 = 'a'

print (id(v1))
print (id(v2))
"""

condicao = False
im_ok = None

if condicao:
    im_ok = True
    print ('ok')
else:
    print ('not ok')
    
print (im_ok, im_ok is None)
print (im_ok, im_ok is not None)