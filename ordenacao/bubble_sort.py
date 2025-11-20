def bubble_sort(array):
    n = len(array)

    # Para cada elemento da lista (controla n° de passadas)
    for i in range(n):
        trocou = False  # flag caso a lista já esteja ordenada

        # Últimos i elementos já estão ordenados (compara pares vizinhos que ainda não estão ordenados)
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Troca os elementos
                array[j], array[j + 1] = array[j + 1], array[j]
                trocou = True

        # caso não haja trocas
        if not trocou:
            break

    return array  


print(bubble_sort([1, 2, 3, 4, 5]))  # Lista já ordenada
print(bubble_sort([5, 4, 3, 2, 1]))  # Lista em ordem reversa
print(bubble_sort([3, 1, 2, 3, 1]))  # Lista com elementos repetidos

