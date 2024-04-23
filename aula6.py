# Operadores Lógicos
entrada = input ('[E]ntrar [S]air: ')
senha_usuario = input ('Senha: ')

senha_permitida = '1234'

print(entrada)

if (entrada == 'E' or entrada == 'e') and senha_usuario == senha_permitida:
    print ('Entrar\n')

else:
    print ('sair\n')


# Falsy (0.0, 0, '')
#avaliação de curto circuito
# print (True and False and True)
#print(True and 0 and True)
#print(True and True and 0.0 and True and False)
#print(True and ' ' and True)
#print(True or False)

#operador not
print (not True)
print (not False)

