# Busca Binária (versão iterativa)
# Complexidade de tempo: O(log n)
# Complexidade de espaço: O(1)
# Requer que a lista esteja ordenada


def pesquisa_binaria_iterativa(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1       # permite igualar ao indicie do último elemento

    # o loop funciona enquanto não chegar a um único elemento
    while esquerda <= direita:
        # divide a lista ao meio, tetornando um valor interiro
        meio = (esquerda + direita) // 2  
        valor_meio = lista[meio]

        # retorna a posição do alvo
        if valor_meio == alvo:
            return meio
    
        if valor_meio > alvo:
            direita = meio - 1
        else:
            esquerda = meio + 1
    
    return None     # -> caso o alvo não esteja na lista


# entradas para teste
lista = [10, 20, 30, 40, 50]

print(f'30 encontrado na posição: {pesquisa_binaria_iterativa(lista, 30)}')  # Esperado: 2
print(f'10 encontrado na posição: {pesquisa_binaria_iterativa(lista, 10)}')  # Esperado: 0
print(f'60 encontrado na posição: {pesquisa_binaria_iterativa(lista, 60)}')  # Esperado: None