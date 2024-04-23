"""
constantes = variáveis q não vão mudar
muitas condições no mesmo If (ruim)
contagem de complexidade (ruim)
"""

# Valores
velocidade_carro = 60 # velocidade atual
local_carro = 101 # local na estrada

V_RADAR_1 = 60 
LOC_RADAR_1 = 100      # em caixa alta esta constante não pode ser mudada 
RADAR_RANGE = 1        # é tipo uma constante no javascript

# variáveis/fórmulas
velocidade_acima = velocidade_carro > V_RADAR_1
carro_passou = local_carro >= (LOC_RADAR_1 - RADAR_RANGE) and \
               local_carro <= (LOC_RADAR_1 + RADAR_RANGE)
carro_multado = carro_passou and velocidade_acima

# body
if velocidade_acima:
    print ('A velocidade do carro passou do radar')

if carro_multado:
    print ('Carro multado')

else: 
    print('Carro não foi multado')