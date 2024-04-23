# Cáculo do IMC
# F-Strings
nome = input ('Digite o seu nome: ')
altura = input ('Digite a sua altura: ')
peso = input ('Digite o seu peso: ')

imc = int(peso) // (float(altura) ** 2)
txt = f'{nome} tem {altura} de altura, pesa {peso} kg e seu IMC é {imc}'


if (imc > 24):
    print (f'\n{nome} você está acima do peso!')
elif (imc < 18.5):
    print (f'\n{nome} você está abaixo do peso!')
else:
    print (f'\n{nome} você está no peso ideal')

print (txt)

# Formatação de Strings com o método format
#a = 'amor'
#b = 'baixinho'
#c = 'coracao'
#d = 10.10

#string = 'a = {3}, b = {1}, c = {0}, d = {nome4}'
#xuxa = string.format(a, b, c, nome4=d)

#print (xuxa)
