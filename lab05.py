##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Gustavo Andrade Taniguchi
# RA: 243651
##################################################

# Leitura do valor da hora
from ast import While

V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
h_trab= 0
h_ex  = 0

while D > 0:
    n = 2*int(input())
    per = []
    while n >=1:
        per.append(int(input()))
        n = n - 1
    
    i = 0
    j = 1
    h = 0
    while j <= len(per):
        h = h + (per[j] - per[i])
        i = i + 2
        j = j + 2
    h_trab = h_trab + h
    if (h > 8):
        h_ex = h_ex + h - 8
    D = D - 1

# Calculo do valor devido ao funcionário
if (h_trab - h_ex - 44) > 0:
    h_ex = h_ex + (h_trab - h_ex - 44)
valor = V*h_trab + (V/2)*h_ex

# Impressão da saída

print("Horas trabalhadas:", h_trab)
print("Horas extras:", h_ex)
print("Valor devido: R$ {:0.2f}".format(valor))