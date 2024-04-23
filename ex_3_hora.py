# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
hora_string = input('Que horas são agora? ')

if hora_string.isdigit():
    hora = int(hora_string)
    dia = hora <= 11
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23
    
    if dia:
        print ('Bom dia!')
    
    elif tarde:
        print ('Boa tarde!')
    
    elif noite:
        print ('Boa noite!')
    
else:
    print ('valor inválido, por favor digite um horário entre 0 e 23 horas')
