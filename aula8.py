# interpolação básica de strings
nome = input('Digite seu nome: ')
preco = input ('Digite o preço: ')
valor = float(preco)

variavel = '%s, o preço é %f' % (nome, valor)
print(variavel)

var = 'HELLO'
print (f'{var}')
print (f'{var:~>22}')
print (f'{var:~<22}')