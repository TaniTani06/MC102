#Listas podem ser criadas de forma implícita listando os elementos entre colchetes, listas podem comportar
#diferentes tipos de dados
frutas = ["Abacaxi","Banana","Caqui"]
#Declarar de forma explícita
a = list(range(10))
empresas = list(["Toyota","Volksvagem","Ford"])

#Acessar o i-ésimo elemento, pode-se usar elementos negativos
print(frutas[0])
#print(frutas[-1])

#len dá o tamanho da lista
print(len(frutas))

#lista[start:stop:step] seleciona parte de uma lista, retorna uma "sublista"
print(frutas[1:4])
print(frutas[::2]) #números de posição pare da lista

#alterar elemento
#lista[i-1]=valor
#lista[start:stop]=[valor_1,...,valor_n] substitui elementos por uma lista

#verificar de o elemento está na lista
#elemento in lista
print("Abacaxi" in frutas)
#True

#append insere elementos no fim da lista
#frutas.append("Limão")
#insert insere em uma posição específico
#frutas.insert(2,"Limão")
#index verifica a posição do elemento na lista
#remove remove a primeira aparicção do elemento em uma lista
#pop remove o elemento na posição dada frutas.pop(1) retorna o elemento removido
#count conta o número de ocorrências de um elemento na lista
#print(paises.count("Brasil"))
#reverse inverte a ordem dos elementos
#sort ordena a lista
a=[5,3]
a.sort()
#sorted obtem uma cópia ordenada de a, sem alterar a lista a original
a=[1]
b = a
b.append(2)
c = b
c.append(3)

#copy retorna uma cópia independente de uma lista
#clonar lista: (nome da lista[start:stop] ou list()
#+ concatena listas


#Tuplas
#listas que não permitem alterações, declarada por ()
#explicitamente: tuple([elemento_1],[elemento_2])
