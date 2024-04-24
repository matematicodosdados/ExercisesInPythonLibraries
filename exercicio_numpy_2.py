import numpy as np
a = np.array([[1,2], [3,4], [5,6]]) # array de rank 1
print(a) # imprimir array
print('Shape:', a.shape) # imprimir shape do array (linhas, colunas)
print('Rank:', a.shape[0]) # imprimir dimensão da array (quantidade de linhas)
print('Primeiro elemento: {0}, Último elemento: {1}'.format(a[0,0],a[2,1])) # imprimindo primeiro e ultimo elemento da array