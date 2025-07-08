def quick_sort(array):
    n = len(array)
    # caso base
    if n < 2:   # lista vazia ou com um único elemento já está ordenada
        return array
    
    pivo = array[0]  # Escolhe o primeiro elemento como pivô

    maiores = []
    menores = []

    # Particiona a lista com base no pivô
    for i in range(1, n):    # Inicia do segundo elemento, pois o primeiro é o pivô
        if array[i] >= pivo:
            maiores.append(array[i])
        else:
            menores.append(array[i])
    
    return quick_sort(menores) + [pivo] + quick_sort(maiores)   # Chamada recursiva para cada sublista




print(quick_sort([1, 2, 3, 4]))       # Já ordenado 
print(quick_sort([4, 3, 2, 1]))       # Reverso
print(quick_sort([3, 1, 2, 3, 1]))    # Com elementos repetidos