#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome:
# RA:
#####################################################
encaixe_original = 0
encaixe_90 = 0
encaixe_180 = 0
encaixe_270 = 0

def giro(trem):
  n = len(trem)
  m = len(trem[0])
  trem_girado = []
  for i in range(m):
    trem_girado.append([])
    for j in range(n):
      (trem_girado[i]).append(trem[- 1 - j][(i)])
  return trem_girado

def verify(tabuleiro, peca, x, y):
  posicao_y = y
  posicao_x = x
  for i in range(len(peca)):
    for j in range(len(peca[i])):
      if (i + posicao_y) == len(tabuleiro) or (j + posicao_x) == (len(tabuleiro[0])):
        break
      if (peca[i][j] == 'X' and tabuleiro[i + posicao_y][j + posicao_x] == 'X'):
        encaixe = False
        break
      else:
        encaixe = True
    if encaixe == False:
      return encaixe
  return encaixe 
'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1) Uma função para rotacionar a peça em 90 graus para direita.
2) Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''

# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

# Processamento

for i in range(len(tabuleiro) + 1 - len(peca)):
  for j in range(len(tabuleiro[0]) + 1 - len(peca[0])):
    if verify(tabuleiro, peca, j, i):
      encaixe_original +=1
    
for i in range(len(tabuleiro) + 1 - len(giro(peca))):
  for j in range(len(tabuleiro[0]) + 1 - len(giro(peca)[0])):
    if verify(tabuleiro, giro(peca), j, i):
      encaixe_90 +=1

for i in range(len(tabuleiro) + 1 - len(giro(giro(peca)))):
  for j in range(len(tabuleiro[0]) + 1 - len(giro(giro(peca))[0])):
    if verify(tabuleiro, giro(giro(peca)), j, i):
      encaixe_180 +=1

for i in range(len(tabuleiro) + 1 - len(giro(giro(giro(peca))))):
  for j in range(len(tabuleiro[0]) + 1 - len(giro(giro(giro(peca)))[0])):
    if verify(tabuleiro, giro(giro(giro(peca))), j, i):
      encaixe_270 +=1

# Impressão do resultado
print(str(encaixe_original) + ',' + str(encaixe_90) + ',' + str(encaixe_180) + ',' + str(encaixe_270))