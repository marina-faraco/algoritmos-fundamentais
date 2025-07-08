from random import randint
from time import time
import selection_sort, bubble_sort, insertion_sort, quick_sort, merge_sort

lista = [randint(0, 10000) for _ in range(10000)]

print('Tempo de execução (segundos)')

# Selection sort
lista_copia = lista.copy()
inicio = time()
selection_sort.selection_sort(lista)
fim = time()
print(f'Selection sort: {fim - inicio:.4f} segundos')

# Bubble sort
lista_copia = lista.copy()
inicio = time()
bubble_sort.bubble_sort(lista)
fim = time()
print(f'Bubble sort: {fim - inicio:.4f} segundos')

# Insertion sort
lista_copia = lista.copy()
inicio = time()
insertion_sort.insertion_sort(lista)
fim = time()
print(f'Insertion:{fim - inicio:.4f} segundos')

# Quick sort
lista_copia = lista.copy()
inicio = time()
quick_sort.quick_sort(lista)
fim = time()
print(f'Quick sort: {fim - inicio:.4f} segundos')

# Merge sort
lista_copia = lista.copy()
inicio = time()
merge_sort.merge_sort(lista)
fim = time()
print(f'Merge sort: {fim - inicio:.4f} segundos')