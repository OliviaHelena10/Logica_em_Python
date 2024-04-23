# Imprecisão dos números de ponto flutuante + round e decimal
num_1 = 0.1
num_2 = 0.7
resultado = num_1 + num_2
print ( resultado )

# formas de contornar a imprecisão do python:
print ( f'{resultado:.2f} ' )
print ( round ( resultado, 3) ) # esse ",3" é a quantidade de casas decimais

# uso da biblioteca decimal
import decimal

num_1 = decimal.Decimal ( 0.1 )
num_2 = decimal.Decimal ( 0.7 )
resultado = num_1 + num_2
print ( resultado ) # esse recurso apenas é bom para casos bem específicos
