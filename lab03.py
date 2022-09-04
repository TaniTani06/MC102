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
preco_vespertino = [30,15,15,15,20,20,30]
preco_noturno = [30,20,20,30,30,40,40]
desconto_vespertino = [0.7,0.5,0.5,0.5,0.5,0.5,0.8]
desconto_noturno = [0.7,0.5,0.5,0.5,0.5,0.7,0.8]

#checar horário
if((time==18 and min<30) or (time<18)):
    ingresso = preco_vespertino[day]
    
    if(s=="S"):
        ingresso = ingresso/2
    else:
        if(c=="C"):
            ingresso = preco_vespertino[day]*desconto_vespertino[day]

if((time==18 and min>=30) or (time>18)):
    ingresso = preco_noturno[day]

    if(s=="S"):
        ingresso = ingresso/2
    else:
        if(c=="C"):
            ingresso = preco_noturno[day]*desconto_noturno[day]

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))