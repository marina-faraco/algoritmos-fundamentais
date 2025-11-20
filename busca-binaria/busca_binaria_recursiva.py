# Busca Binária (versão recursiva)
# Complexidade de tempo: O(log n)
# Complexidade de espaço: O(1)
# Requer que a lista esteja ordenada

def pesquisa_binaria_recursiva(lista, alvo, esquerda, direita):
    # caso base
    if esquerda > direita:
        return None
    
    # separa a lista ao meio
    meio = (esquerda + direita) // 2

    # checa se o meio é o elemento desejado
    if lista[meio] == alvo:
        return meio
    
    # senão verifica se o meio é maior ou menor que o elemento desejado
    elif lista[meio] > alvo:    
       return pesquisa_binaria_recursiva(lista, alvo, esquerda, meio - 1)   # -> recurção
    
    else:
       return pesquisa_binaria_recursiva(lista, alvo, meio + 1, direita)    # -> recurção
   

# entradas para teste
lista = [10, 20, 30, 40, 50]

esquerda = 0
direita = len(lista) - 1

print(f'30 encontrado na posição: {pesquisa_binaria_recursiva(lista, 30, esquerda, direita)}')  # Esperado: 2
print(f'10 encontrado na posição: {pesquisa_binaria_recursiva(lista, 10, esquerda, direita)}')  # Esperado: 0
print(f'60 encontrado na posição: {pesquisa_binaria_recursiva(lista, 60, esquerda, direita)}')  # Esperado: None
