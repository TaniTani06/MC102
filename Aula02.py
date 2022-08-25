from tarfile import TarInfo


print ("Hello","world!", )
#sep define qual será a separação
#end define qual será o caracter ao fim do comando
# # comenta
print ("Unicamp", "MC102",sep="-", end= "!")
'''Três aspas comentam o que está entre elas (fica vermelho)'''

##Variáveis:
#int:   inteiros
#float: reais
#str:   cadeia de caracteres/string
#bool:  Valores booleanos: True/False

#type (função) - mostra o tipo da variável
print(type(10))
#<class 'float'>

# = atribui um valor para variáveis
a = b = c = 3
print(a,b,c)
a, b, c = 1, 2, 3
print(a, b, c)

#NOMES DE VARIÁVEIS
#Devem começar por uma letra ou um sublinhado
#Python é uma linguagem sensitive = diferencia letra maiúscula e minúscula

#OPERADORES MATEMÁTICOS
# +, -, *, /, // (divisão inteira), ** (exponenciação), % (módulo=resto da divisão inteira).
print(10 // 3)
print(2 ** 10)
# x +=y equivale a x = x + y
d = 100
d+= 50
print(d)
#precedência é a ordem que os operadores são avaliados, sendo ela: **, */, %, +-. parênteses funcionam!

#OPERAÇÃO COM STRINGS
#Concatenação +
nome = "Tani"
mensagem = ", Olá!"
print(nome + mensagem)
#Replicação *
print(nome*2 + "06")
#Ordem: Replicação>Concatenação

#Comparações numéricas: <, >, <=, >=, != (diferente), == (igual)
print(5 <= 4)
print(5 != 4)
#também funciona para strings
print("a">"b")
print("Abacate">"Absurdo")

print("--------")

#OPERADORES LÓGICOS: and, or, not. & ("e" n preguiçoso), | ("or" n preguiçoso)
#com not>and>or
print(True and False)
print(3<4 and "banana">"abacaxi")
n="-----------"
print(n)
print(True or False)
print(False or False)
print(n)
print(not True and False)
print(not (True and False))

#Conversões de tipos (cast)
#int(), float(), str(), bool()
print(n)
print(int(True))

#input recebe dados do usuário
print(n)
day=input("Qual a data é hoje? ")
print("Então hoje é " + day)