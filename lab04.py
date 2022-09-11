###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Gustavo Andrade Taniguchi   
# RA: 243651
###################################################

# leitura da sequência de compras e vendas

estoque = 0
vendas = 0
x = int(input())

while x != 0:
    if x > 0:
        estoque = estoque + x
    else:
        if (x*(-1)) < estoque:
            estoque = estoque + x
            vendas = vendas + 1
        else:
            y=str(-x)
            print("Quantidade indisponível para a venda de " + y + " unidades.") 
    x = int(input())

# impressão da saída
if((x)==0):
    print("Quantidade de vendas realizadas: " + str(vendas))
    print("Quantidade em estoque: " + str(estoque))