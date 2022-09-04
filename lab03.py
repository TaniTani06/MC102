###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Gustavo Andrade Taniguchi   
# RA: 243651
###################################################

# leitura de dados

day = int(input())
time = int(input())
min = int(input())
s = input()
c = input()
price = 0

if(c== "D"):
    c= False

# valor do ingresso inteiro
if(time>18):
    if(day==1 or day==4 or day==5):
        price = 30
    
    if(day==2 or day==3):
        price = 20
    
    if(day==6 or day==7):
        price = 40

if(time<18):
    if(day==1 or day==7):
        price = 30
    
    if(day==2 or day==3 or day==4):
        price = 15
    
    if(day==5 or day==6):
        price = 20

if(time==18):
    if(min<30):
        if(day==1 or day==7):
            price = 30
        
        if(day==2 or day==3 or day==4):
            price = 15
        
        if(day==5 or day==6):
            price = 20

    if(min>=30):
        if(day==1 or day==4 or day==5):
            price = 30
    
        if(day==2 or day==3):
            price = 20
    
        if(day==6 or day==7):
            price = 40




# valor a pagar
if(s=="S"):
    price = price/2

else:
    if(c=="C"):
        if(time>18):
            if(day==1 or day==6):
                price = price*0.7
            
            if(day==2 or day==3 or day==4 or day==5):
                price = price*0.5

            if(day==7):
                price = price*0.8
        
        if(time<18):
            if(day==1):
                price = price*0.7
            
            if(day==2 or day==3 or day==4 or day==5 or day==6):
                price = price*0.5

            if(day==7):
                price = price*0.8
        
        if(time==18):
            if(min<30):
                if(day==1):
                    price = price*0.7
            
                if(day==2 or day==3 or day==4 or day==5 or day==6):
                    price = price*0.5

                if(day==7):
                    price = price*0.8

            if(min>=30):
                if(day==1 or day==6):
                    price = price*0.7
            
                if(day==2 or day==3 or day==4 or day==5):
                    price = price*0.5

                if(day==7):
                    price = price*0.8

ingresso = price


# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))