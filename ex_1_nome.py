nome = input ('Qual o seu nome? ')
id = input ('Qual a sua idade? ')

if nome !='' and id != '':
    print (f'Seu nome é {nome}')
    print (f'Seu nome invertido é {nome[-1:-100:-1]}')
    
    if ' ' in nome:
        print ('Seu nome contém espaços')
    else:
        print ('Seu nome não contém espaços')
    
    print (f'Seu nome tem {len(nome)} caracteres')
    print (f'A primeira letra do seu nome é {nome[0]}')
    print (f'A ultima letra do seu nome é {nome[-1]}')
else:
    print ('Desculpe, você deixou campos vazios')