while True:
    num_1 = input ( 'Digite um número: ' )
    num_2 = input ( 'Digite outro número: ' )
    operador = input ( 'Digite o operador ( +, -, *, /): ' )
    
    numeros_validos = None # o valor None, representa a ausência de um valor definido. 
                           # Isso é útil para indicar que ainda não verificamos se os números digitados 
                           # pelo usuário são válidos ou não.
                           # None --> para indicar que ainda não realizamos a verificação.
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float ( num_1 )
        num_2_float = float ( num_2 )
        numeros_validos = True
        
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print ( '1 ou mais termo(s) digitado(s) inválido(s)' )
        break
        
    operadores_permitidos = '+-*/'
        
    if operador not in operadores_permitidos:
        print ( 'Operador inválido' )
        break
        
    if len(operador) > 1:
        print ( 'Digite apenas um operador' )
        break
        
    if operador == '+':
        print ( num_1_float + num_2_float )
        
    elif operador == '-':
        print ( num_1_float - num_2_float )
        
    elif operador == '*':
        print ( num_1_float * num_2_float )
        
    elif operador == "/":
        print ( num_1_float / num_2_float )
            
    else:
        print ( 'Houve um erro' )
        break
        
    sair = input( 'Vc quer sair? ' ).lower().startswith( 's' or 'S' or 'sim' or 'Sim' )
        
    if sair is True:
        print ( 'Você saiu' )
        break
    else:
        print ( "Houve um erro, tente novamente" )