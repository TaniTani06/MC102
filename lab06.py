##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Gustavo Nadrade Taniguchi
# RA: 243651
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos
n=int(input())
while n>0:
   move=torre[0:n]
   move.reverse()
   torre[:n]=move
   n=int(input())

# Impressão da saída
if (sorted(torre) == torre):
   print("Torre estavel")
else:
   print("Torre instavel")