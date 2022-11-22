###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Gustavo Andrade Taniguchi  
# RA: 243651
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    a = 0
    m = len(imagem_original[0])
    n = len(imagem_original)
    imagem = []
    for i in range(2*n-1):
        imagem.append([])
        for j in range(2*m-1):
            imagem[i].append(a)
            a += 1
    for i in range(n):       #Passo 1
        for j in range(m):
            imagem[2*i][2*j] = imagem_original[i][j]
    for i in range(0,2*n,2):       #Passo 2
        for j in range(1,2*m-1,2):
            imagem[i][j] = int((imagem[i][j-1] + imagem[i][j+1])/2)
    for i in range(1,2*n-1,2):
        for j in range(0,2*m,2):   #Passo 3
            imagem[i][j] = int((imagem[i+1][j]+imagem[i-1][j])/2)
    for i in range(1,2*n-1,2):
        for j in range(1,2*m-1,2): #Passo 4
            imagem[i][j] = int((imagem[i-1][j-1] + imagem[i-1][j+1] + imagem[i+1][j-1] + imagem[i+1][j+1])/4)
    return imagem

def retracao(imagem_original):
    a = 0
    m = len(imagem_original[0])
    n = len(imagem_original)
    imagem = []
    for i in range(1,n,2):
        imagem.append([])
        for j in range(1,m,2):
            a = int((imagem_original[i-1][j-1] + imagem_original[i][j-1] + imagem_original[i-1][j] + imagem_original[i][j])/4)
            imagem[int((i-1)/2)].append(a)

    if (n%2) != 0 and (m%2) != 0: #ímpar e ímpar
        imagem.append([])
        for j in range(1,m,2):
            imagem[-1].append(int((imagem_original[-1][j-1] + imagem_original[-1][j])/2))
        for i in range(1,n,2):
            imagem[int((i-1)/2)].append(int((imagem_original[i-1][-1] + imagem_original[i][-1])/2))
        imagem[-1].append(imagem_original[-1][-1])

    if (n%2) != 0 and (m%2) == 0: #ímpar e par
        imagem.append([])
        for j in range(1,m,2):
            imagem[-1].append(int((imagem_original[-1][j-1] + imagem_original[-1][j])/2))

    if (n%2) == 0 and (m%2) != 0: #par e ímpar
        for i in range(1,n,2):
            imagem[int((i-1)/2)].append(int((imagem_original[i-1][-1] + imagem_original[i][-1])/2))
    return imagem
# leitura da imagem
_ = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

_ = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento
tipo = str(input())
if tipo == 'expansao' :
    imagem = expansao(imagem_original)
else:
    imagem = retracao(imagem_original)

# impressão da imagem final
imprimir_imagem(imagem)