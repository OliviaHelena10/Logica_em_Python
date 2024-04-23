# iterável
# iterador -> qm entrega um valor por vez
# next ->
# iter ->

texto = "Olívia"
iterador = iter(texto)

while True:
    
    try:
        print (next(iterador))
        
    except StopIteration:
        break
        

