###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Gustavo Andrade Taniguchi
# RA: 243651
###################################################

# Leitura das tropas de defesa
n=int(input())
defesa = []
for i in range(n):
    defesa.append(int(input()))
    
# Leitura das tropas de ataque
n=int(input())
ataque = []
for i in range(n):
    ataque.append(int(input()))

# Processamento da guerra
derrota = True
posicao = 1
while derrota == True:
    batalhas = 0
    for i in range(len(ataque)):
        if ataque[i] > defesa[i]:
            batalhas += 1
        if ataque[i] == defesa[i]:
            batalhas += 0
        if ataque[i] < defesa[i]:
            batalhas += -1
    if batalhas > 0:
        derrota = False
        break
    else:
        posicao += 1
        del defesa[0]
        if len(defesa) < len(ataque):
            break

# Saída de dados
if derrota == True:
    print('Derrota')

else:
    print('Vitória posicionando as tropas a partir da posição', posicao)