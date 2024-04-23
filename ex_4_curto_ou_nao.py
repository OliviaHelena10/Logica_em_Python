# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
nome = input ('Digite o seu nome: ')
tamanho = len(nome)
curto = tamanho < 5  and tamanho >=1
normal = tamanho > 4 and tamanho < 7
grande = tamanho > 6 

if curto:
    print ('Seu nome é curto')

elif normal:
    print ('Seu nome é normal')

elif grande:
    print ('Seu nome é muito grande')

else:
    print ('Por favor, digite algo')