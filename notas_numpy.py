import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
slice = a[:2, 1:3] #pegando os elementos da 2 linha e colunas 1,2
print(slice)
slice[0,0] = 53 #pegando o elemento (0,0) da array fatiada
print(slice)
print(a) #A array e a sua partição tem o mesmo ponteiro! 

linha_r1 = a[1, :] #subarray da linha 2 com rank1
linha_r3 = a[2:3, :] # subarray da linha 4 com rank3

#zerando todos os elementos de a > 6
a[a>6] = 0 
print(a)

#Somando com arrays
x = np.array([[1,2],[3,4]])
soma = x + 10 
print(soma)

#subtraindo com arrays
subtra = np.subtract(x,1)
print(subtra)

#multiplicando
mult = x*10
print(mult)

#dividindo
divisao = np.divide(x,10)
print(divisao)

#as mesmas operações podem ser feitas de array para array, exceto a multiplicação que se usa np.dot(x,v), onde x e v são matrizes ou arrays multimensionais (é a mesma coisa)

x = np.array([[1.,2.],[3.,4.]])
y = np.array([[5.,6.],[7.,8.]])

#As seguintes operações entre matrizes calculam os elementos das matrizes em uma mesma posição, isto é, fazem operações com (x0, y0) das matrizes e no fim retornam uma outra matriz já com as operações feitas

#soma
soma = x + y
soma = np.add(x, y)
print(soma)

#subtração
subt = np.subtract(x,y)
print(subt)

#multiplicação de ELEMENTOS!

mult = x*y 
print(mult)

#divisao (O mesmo caso que o acima)

divisao = np.divide(x,y)
print(divisao)

#Observação, pelo modo que é dado as operações, as operações aritmeticas só funcionam para matrizes de mesmo tamanho.

#Multiplicação de matrizes (agora realmente o é)

x = np.array([[1,2],[3,4]])
v = np.array([[9],[10]])

x.dot(v)
matriz_resultante = np.dot(x,v)
print(matriz_resultante)

#Outras funções

m = np.array([[1,2, 3, 4],[10, 20, 30, 40]])

print(m)

#soma de todos os elementos de x
print(np.sum(m))

#soma dos elementos de cada coluna -> retorna uma lista com a soma dos elementos de cada coluna
print(np.sum((m), axis=0))

#soma dos elementos de cada linha -> retorna uma lista com a soma dos elementos de cada linha
print(np.sum(m, axis=1))

#Transposta de uma matriz
a = np.array([[1,2], [3, 4], [5, 6]])
print("Transposta da matriz \n {0} \né \n{1}".format(a, a.T))

#importando arquivos com numpy

#Use a função np.loadtext('base.csv' ,delimiter=',', dtype=np.float64)
