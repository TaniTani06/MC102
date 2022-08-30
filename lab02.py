###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Gustavo Andrade Taniguchi  
# RA: 243651
###################################################

# Leitura de dados

d1 = int(input())
v1 = int(input())
t  = int(input())
d2 = int(input())
v2 = int(input())




# Cálculo do tempo total gasto por cada espaçonave 

t1 = d1/v1
t2 = (t*24 + d2/v2)



# Impressão da resposta

print(t1<t2)