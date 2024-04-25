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
