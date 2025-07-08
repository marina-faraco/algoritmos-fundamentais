def insertion_sort(array):
    n = len(array)
    # caso base
    if n < 2:  # Lista vazia ou com um único elemento já está ordenada
        return array

    for i in range(1, n):   # Percorre a lista a partir do segundo elemento
        valor = array[i]    # Salva o valor atual a ser posicionado
        j = i - 1           # Começa comparando com o elemento anterior
        
        while j >= 0 and array[j] > valor:  
            array[j + 1] = array[j]  # Empurra o elemento maior uma posição à frente
            j -= 1                   # Avança para o elemento anterior

        array[j + 1] = valor  # Insere o valor na posição correta
    return array


print(insertion_sort([1, 2, 3, 4]))       # Já ordenado 
print(insertion_sort([4, 3, 2, 1]))       # Reverso
print(insertion_sort([3, 1, 2, 3, 1]))    # Com elementos repetidos
