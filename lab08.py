###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Gustavo Andrade Taniguchi
# RA: 243651
###################################################

# Leitura da palavra
palavra = input()
# Leitura dos palpites e impressão do resultado para cada palpite
tent = 0
while tent < 6:
    impressao = ''
    palpite = input()
    saida = []
    if palpite == palavra:
        print(palpite.upper())
        print("Resposta correta")
        break
    else:
        for i in range (len(palavra)):
            if palavra[i] == palpite[i]:
                PALPITE = palpite.upper()
                saida.append(PALPITE[i])
            else:
                if palpite[i] in palavra:
                    saida.append(palpite[i])
                else:
                    saida.append('_')
        for i in saida:
            impressao += i
        print (impressao)
        tent += 1
            

# Impressão da linha final
if tent == 6:
    print("Palavra correta:", palavra)