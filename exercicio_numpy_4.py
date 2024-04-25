import numpy as np
 
# a) Crie um array do numpy, com duas linhas e 5 colunas com valores 
#    float (não esqueça de usar o parâmetro **dtype**) de sua escolha.

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=np.float64)
print('Array:\n', array)

# b) a soma dos elementos das linhas do array

soma = np.sum(array, axis=1, keepdims=True)
print('Soma dos elementos das linhas do array:\n', soma)

# c) a multiplicação dos elementos das colunas do array

mult = np.prod(array, axis=0, keepdims=True)
print('Multiplicação dos elementos das colunas do array:\n', mult)


# d) a média de todos elementos do array

media = np.mean(array)
print('Média de todos elementos do array:\n', media)


# e) a média dos elementos das linhas do array

media_linha = np.mean(array, axis=1, keepdims=True)
print('Média dos elementos das linhas do array:\n', media_linha)


# f) a média dos elementos das colunas do array

media_coluna = np.mean(array, axis=0, keepdims=True)
print('Média dos elementos das colunas do array:\n', media_coluna)


# g) o desvio padrão de todos elementos do array

desvio = np.std(array)
print('Desvio padrão de todos elementos do array:\n', desvio)


# h) o desvio padrão das linhas do array

desvio_linha = np.std(array, axis=1, keepdims=True)
print('Desvio padrão das linhas do array:\n', desvio_linha)


# i) o desvio padrão dos elementos das colunas do array

desvio_coluna = np.std(array, axis=0, keepdims=True)
print('Desvio padrão das colunas do array:\n', desvio_coluna)