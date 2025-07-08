def selection_sort(array):
    n = len(array)

    for i in range(n):
        # Determina i como a posição min
        min_index = i

        for j in range(i + 1, n):
            # Compara a posição atual com a min
            if array[j] < array[min_index]:
                min_index = j
        # Realiza a troca
        array[i], array[min_index] = array[min_index], array[i]

    return array


print(selection_sort([1, 2, 3, 4]))       # Já ordenado 
print(selection_sort([4, 3, 2, 1]))       # Reverso
print(selection_sort([3, 1, 2, 3, 1]))    # Com elementos repetidos
