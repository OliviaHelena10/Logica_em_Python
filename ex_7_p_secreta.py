"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.

- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.

    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
    
Faça a contagem de tentativas do seu
usuário.
"""
import os
import time

print ('---------------------------------')
print ('\n   ADIVINHE A PALAVRA SERCRETA')
print ('\n---------------------------------')
time.sleep(3)
os.system('cls')

palavra_secreta = 'programador'
letra_certa = ''
num_tentativas = 0


while True:
    
    letra_user = input('\nDigite uma letra: ')
    num_tentativas += 1
    
    if len(letra_user) > 1:
        print ('por favor, digite apenas uma letra.')
        continue
    
    if letra_user in palavra_secreta:
        letra_certa += letra_user

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        
        if letra_secreta in letra_certa:
             palavra_formada += letra_secreta
             
        else:
            palavra_formada += '*'
            
    print (palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print ('\n\n----------------------------------')
        print ('\n          PARABÉNS!!!!\n         Fim de Jogo :D')
        print ('\n----------------------------------')
        print (f'\nA palavra era: "{palavra_secreta}"')
        print (f'\nTentativas: {num_tentativas}\n')
        break
        
    else:
        print ('continue!')
    