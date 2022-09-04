###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Gustavo Andrade Taniguchi   
# RA: 243651
###################################################

# leitura de dados

day = int(input()) - 1
time = int(input())
min = int(input())
s = input()
c = input()

# valor do ingresso inteiro
pv = [30,15,15,15,20,20,30]
pn = [30,20,20,30,30,40,40]
dv = [0.7,0.5,0.5,0.5,0.5,0.5,0.8]
dn = [0.7,0.5,0.5,0.5,0.5,0.7,0.8]

#checar horário
if((time==18 and min<30) or (time<18)):
    ingresso = pv[day]
    
    if(s=="S"):
        ingresso = ingresso/2
    else:
        if(c=="C"):
            ingresso = pv[day]*dv[day]

if((time==18 and min>=30) or (time>18)):
    ingresso = pn[day]

    if(s=="S"):
        ingresso = ingresso/2
    else:
        if(c=="C"):
            ingresso = pn[day]*dn[day]

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))