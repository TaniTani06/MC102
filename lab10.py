#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Gustavo Andrade Taniguchi
# RA: 243651
#####################################################

from copy import deepcopy

# Leitura da matriz
tesouros_1 = 0
tesouros_2 = 0
n = int(input())
matriz = [input().split() for _ in range(n)]
mapa = deepcopy(matriz)
# Leitura e processamento dos caminhos
time_1 = str(input())
if time_1 == 'azul':
    time_2 = 'vermelho'
else:
    time_2 = 'azul'
M = int(int(input())/2)

for m in range (M):
    x = 0
    y = 0
    caminho_1 = str(input())
    for mov in caminho_1:
        if mov == 'N':
            y -= 1
        if mov == 'S':
            y += 1
        if mov == 'L':
            x += 1
        if mov == 'O':
            x -= 1
        pos = mapa[y][x]
        if pos == '*':
            tesouros_1 +=1
            mapa[y][x] = "."
    x = 0
    y = 0
    caminho_2 = str(input())
    for mov in caminho_2:
        if mov == 'N':
            y -= 1
        if mov == 'S':
            y += 1
        if mov == 'L':
            x += 1
        if mov == 'O':
            x -= 1
        pos = mapa[y][x]
        if pos == '*':
            tesouros_2 +=1
            mapa[y][x] = "."

# Impressão da saída
if time_1 == 'azul':
    print('Tesouros encontrados pelo time azul: ' + str(tesouros_1))
    print('Tesouros encontrados pelo time vermelho: ' + str(tesouros_2))
else:
    print('Tesouros encontrados pelo time azul: ' + str(tesouros_2))
    print('Tesouros encontrados pelo time vermelho: ' + str(tesouros_1))

if tesouros_1 > tesouros_2:
    print('Vitoria do time ' + time_1)
if tesouros_1 == tesouros_2:
    print('Empate')
if tesouros_1 < tesouros_2:
    print('Vitoria do time ' + time_2)