###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Gustavo Andrade Taniguchi
# RA: 243651
###################################################

from collections import OrderedDict

# Leitura de dados + processamento
estoque = {}
compra = {}
venda = {}
while True:
    leitura = input()
    if leitura == "FIM":
        estoque_ord = OrderedDict(sorted(estoque.items()))
        break
    pedido = leitura.split(' : ')
    produto = pedido[0]
    quant = int(pedido[1])
    if produto in estoque.keys():
        if ((estoque[produto] + quant) >= 0):
            estoque[produto] += quant
            if quant > 0:
                compra[produto] += 1
            else:
                if produto in venda.keys():
                        venda[produto] += 1
        else:
            X = str(-quant)
            print("Quantidade indisponivel para a venda de " + X + " unidade(s) do produto " + produto + ".")
    else:
        if quant > 0:
            estoque[produto] = quant
            compra[produto] = 1
            venda[produto] = 0
        else:
            X = str(-quant)
            print("Quantidade indisponivel para a venda de " + X + " unidade(s) do produto " + produto + ".")

# Ordenação
# Impressão da saída
for produto in estoque_ord.keys():
    print("Produto: " + produto)
    E = str(estoque_ord[produto])
    print("Quantidade em Estoque: " + E)
    print("Pedidos de Compra: " + str(compra[produto]))
    print("Pedidos de Venda: " + str(venda[produto]))