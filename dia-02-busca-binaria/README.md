# O que é busca binária

A **busca binária** é um algoritmo eficiente para encontrar um elemento em uma lista **ordenada**.

Ela funciona dividindo repetidamente a lista ao meio, comparando o elemento central com o valor buscado. Com base no resultado da comparação, elimina metade da lista — mantendo apenas a parte onde o elemento pode estar.

---

# Diferença entre abordagem iterativa e recursiva

Ambas as abordagens seguem a mesma lógica, mas se diferenciam na forma de implementação:

- **Iterativa**: utiliza estruturas de repetição, como o `while`, para controlar o fluxo do algoritmo.
- **Recursiva**: a própria função chama a si mesma, reduzindo o escopo da busca a cada chamada até encontrar o valor (ou até não restarem mais elementos).

---

# Complexidade: O(log n)

A complexidade da busca binária é **O(log n)**, também chamada de **tempo logarítmico**.

Isso significa que, à medida que o tamanho da lista cresce, o número de comparações necessárias **não cresce na mesma proporção**. Por exemplo:

- Em uma lista com 1.000 elementos, bastam no máximo cerca de 10 comparações.
- Já na busca linear (O(n)), seria necessário até 1.000 comparações no pior caso.

Em listas pequenas, essa diferença pode parecer irrelevante. Mas, em listas grandes, a eficiência da busca binária se torna extremamente vantajosa.

---

# Quando a busca binária é melhor que a linear

A busca binária é **mais eficiente** do que a busca linear em **listas grandes e ordenadas**.

> ⚠️ Importante: se a lista não estiver ordenada, a busca binária **não funciona** corretamente.

---

# Exemplos de uso no dia a dia

### 📚 Procurar uma palavra no dicionário

Ao buscar uma palavra no dicionário físico, você **não começa da primeira página**, mas sim vai direto à seção com a letra inicial da palavra. Isso reduz drasticamente a quantidade de páginas a serem verificadas.

### 📱 Procurar um contato no celular

Nos aplicativos de contatos, os nomes estão em **ordem alfabética**. Ao digitar as primeiras letras do nome, o aplicativo **filtra os contatos possíveis**, eliminando todos os outros automaticamente — uma lógica muito parecida com a busca binária.

---

# Casos de teste

```python
lista = [10, 20, 30, 40, 50]

print(f'30 encontrado na posição: {pesquisa_binaria(lista, 30)}')  # Esperado: 2
print(f'10 encontrado na posição: {pesquisa_binaria(lista, 10)}')  # Esperado: 0
print(f'60 encontrado na posição: {pesquisa_binaria(lista, 60)}')  # Esperado: None
