# entrada para teste
lista = [10, 20, 30, 40]
alvo = 30

# for passa por cada item da lista
for i in range(len(lista)):
    # se o item for igual ao alvo, mostrar posiçao do item
    if lista[i] == alvo:
        print(f'Valor encontrado na posição {i}')
        break

# senão, o item não está presente na lista.
else:
    print('Valor não encontrado.')
