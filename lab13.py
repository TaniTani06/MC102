###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Gustavo Andrade Taniguchi
# RA: 243651
###################################################

# Leitura de dados
candidatos = {"Branco": 0, "Nulo": 0}
while True:
    x = str(input())
    if x == '0':
        break
    if x in candidatos.keys():
        candidatos[x] += 1
    else:
        candidatos[x] = 1

# Saída de dados
a = sorted(candidatos.items(), key=lambda x: x[1], reverse=True)
for i in a:
    if (str(i[0]) != 'Branco') and (str(i[0]) != 'Nulo'):
        print(str(i[0]) + ' ' + str(i[1]))
print('Brancos ' + str(candidatos['Branco']))
print('Nulos ' + str(candidatos['Nulo']))