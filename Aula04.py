#while evita o uso de vários "if"
n=1
while n <= 10:
    print(n)
    n = n + 1

#Lista: estrutura que armazena múltiplos dados
#lista = [<dado_1>,<dado_2>,...]
#print lista[0] imprime o valor 0 da lista com o nome "lista"
#len() retorna o número de elementos da lista

letras = ["A","B","C","D","E","F","G"]
i=0
while i< len(letras):
    print(letras[i])
    i=i+1

#máximo
numeros = [3,1,7,9,4]
maximo=0

i=0
while i< len(numeros):
    if numeros[i]>maximo:
        maximo=numeros[i]
    i=i+1
print(maximo)

#for <variavel> in <lista>, repete os valores da lista até que todos sejam percorridos
for letra in letras:
    print(letra)
#pode-se usar for <variavel> in range () para definir um range pra atuação do for 
#(inclui o primeiro e exclui o ultimo)
