import numpy as np
ar = np.array([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,3,4,0], [0,0,0,0]])
print(ar)
slice = ar[2:4, 1:3] #fatiamento que gera a subarray [[1,2], [3,4]]
print(slice)
