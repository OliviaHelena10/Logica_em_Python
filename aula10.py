"""
Introdução ao try e except para capturar erros (exceptions)

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input ('Vou dobrar o número q vc digitar\nDigite o número: ')

try:
#print ('STR: ', numero_str)
    numero = (float(numero_str))
#print ('Float: ', numero)
    print (f'O dobro do numero {numero_str} é {numero * 2}.')

except:
    print (f'"{numero_str}" não é um número!')

"""
if numero.isdigit:
    numero_float = float(numero)
    print (f'O dobro de {numero} é {numero_float * 2}')
else:
    print ('Inválido, por favor digite um número')
"""