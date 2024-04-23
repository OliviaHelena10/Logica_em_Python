import os

lista = []

while True:
    print ( 'Selecone uma opção' )
    opcao = input( '\n[a]inserir\t[b]apagar\t[c]encerrar\n' )
    
    if opcao == 'a':
        os.system ( 'clear' )
        adiciona = input ( 'Digite o que deseja adionar: ' )
        lista.append( adiciona )
    
    elif opcao == 'b':
        os.system ( 'clear' )
        tira_str = input(' Digite o índice do item que deseja retirar: ' ).lower
       
        try:
            indice = int ( tira_str )
            del lista [indice]
            
        except ValueError:
            print ( "Por favor, digite um número inteiro." )
        
        except IndexError:
            print ( "Essa opção não existe.")
        
        except Exception:
            print ( 'Erro desconhecido' )
        
    elif opcao == 'c':
        os.system ( 'clear' )
        print ( 'Sua lista ficou assim: ' )
        
        for indice, texto in enumerate ( lista ):
            print ( indice, texto )
            
    else:
        print ( 'Inválido. Por favor, selecione uma das opções' )
