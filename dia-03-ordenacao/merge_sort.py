def merge_sort(array):
    n = len(array)

    # caso base 
    if n < 2:  # Lista vazia ou com um único elemento já está ordenada
        return array
    
    meio = n // 2   # divide a lista em duas partes
    esquerda = array[:meio]
    direita = array[meio:]

    # chamada recursiva para ordenr cada mescla
    esq = merge_sort(esquerda)  
    dir = merge_sort(direita)
    
    # combina as duas metades ordenadas
    return merge(esq, dir)
    


def merge(array1, array2):
    resultado = []

    # enquanto ambas listas tiverem elementos
    while len(array1) != 0 and len(array2) != 0:
        # combara o 1° elemento de cada lista
        if array1[0] <= array2[0]:
            # adiciona o menos à lista e remove da lista original
            resultado.append(array1[0])
            del array1[0]
        else:
            resultado.append(array2[0])
            del array2[0]

    # quando uma das listas estiver vazia, adiciona o restante da outra
    return resultado + array1 + array2
    


print(merge_sort([1, 2, 3, 4]))       # Já ordenado 
print(merge_sort([4, 3, 2, 1]))       # Reverso
print(merge_sort([3, 1, 2, 3, 1]))    # Com elementos repetidos