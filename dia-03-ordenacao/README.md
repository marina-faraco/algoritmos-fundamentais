# 📊 **Algoritmos de Ordenação**

Este documento apresenta os principais algoritmos de ordenação, com explicações, complexidades, uso ideal e comparação entre eles.

---

## 🔹 Descrição dos Algoritmos

### 🔸 Bubble Sort
Compara pares de elementos 'vizinhos' e os troca de lugar se estiverem fora de ordem. Repete o processo até que a lista esteja ordenada.

> 💡 O maior valor "borbulha" até o final da lista a cada iteração.

---

### 🔸 Selection Sort
Encontra o menor elemento da lista e o coloca na posição correta. Repete o processo com o restante da lista.

> 💡 Seleciona o menor a cada passo e o coloca na posição certa.

---

### 🔸 Insertion Sort
Constrói a lista ordenada uma peça por vez, comparando o elemento atual com os anteriores e inserindo-o na posição correta.

> 💡 "Empurra" a lista para o lado, inserindo o elemento na posição adequada.

---

### 🔸 Quick Sort
Escolhe um pivô e reorganiza a lista de forma que os menores fiquem à esquerda e os maiores à direita. Aplica o mesmo processo recursivamente às sublistas.

> 💡 Divide e conquista com foco em partição ao redor do pivô.

---

### 🔸 Merge Sort
Divide a lista em partes até restarem listas com um único elemento e, em seguida, as funde de forma ordenada até reconstruir a lista original.

> 💡 Divide e conquista, com foco em mesclar listas ordenadas.

---

## ⚙️ Complexidades de Tempo

| Algoritmo         | Tempo Médio     | Pior Caso       | Melhor Caso     |
|-------------------|------------------|------------------|------------------|
| **Bubble Sort**    | O(n²)            | O(n²)            | O(n)             |
| **Selection Sort** | O(n²)            | O(n²)            | O(n²)            |
| **Insertion Sort** | O(n²)            | O(n²)            | O(n)             |
| **Quick Sort**     | O(n log n)       | O(n²)            | O(n log n)       |
| **Merge Sort**     | O(n log n)       | O(n log n)       | O(n log n)       |

---

## 🧠 Complexidade de Espaço

| Algoritmo         | Espaço Extra | In-place? | Estável? | Observação |
|-------------------|--------------|-----------|----------|------------|
| **Bubble Sort**    | O(1)         | ✅ Sim    | ✅ Sim   | Usa apenas variáveis auxiliares |
| **Selection Sort** | O(1)         | ✅ Sim    | ❌ Não   | Poucas trocas, mas não estável |
| **Insertion Sort** | O(1)         | ✅ Sim    | ✅ Sim   | Ótimo para listas quase ordenadas |
| **Quick Sort**     | O(log n)¹    | ⚠️ Parcial| ❌ Não   | Pode chegar a O(n) se não otimizado |
| **Merge Sort**     | O(n)         | ❌ Não    | ✅ Sim   | Cria listas auxiliares |

> ¹ Quick Sort usa pilha de recursão. No pior caso, pode chegar a O(n).

---

## ✅ Melhor Uso Prático

| Algoritmo         | Melhor Uso Prático                                                                 |
|-------------------|-------------------------------------------------------------------------------------|
| **Bubble Sort**    | Listas **muito pequenas** ou para **fins didáticos**. Pouco eficiente em geral.    |
| **Selection Sort** | Listas **pequenas** com **poucas trocas**.                                         |
| **Insertion Sort** | Listas **pequenas ou quase ordenadas**. Muito rápido no melhor caso.               |
| **Quick Sort**     | Listas **grandes** com **bom pivô**. Desempenho excelente na média.                |
| **Merge Sort**     | Listas **grandes**, quando **estabilidade** é importante ou com **dados externos**.|

---

## 📋 Tabela Comparativa Geral

| Algoritmo         | Tempo Médio | Pior Caso | Espaço Extra | Estável? | In-place? | Melhor Uso Prático                      |
|-------------------|-------------|-----------|---------------|----------|-----------|------------------------------------------|
| **Bubble Sort**    | O(n²)       | O(n²)     | O(1)          | ✅ Sim   | ✅ Sim    | Listas muito pequenas ou fins didáticos  |
| **Selection Sort** | O(n²)       | O(n²)     | O(1)          | ❌ Não   | ✅ Sim    | Listas pequenas com poucas trocas        |
| **Insertion Sort** | O(n²)       | O(n²)     | O(1)          | ✅ Sim   | ✅ Sim    | Listas pequenas ou quase ordenadas       |
| **Quick Sort**     | O(n log n)  | O(n²)     | O(log n)¹     | ❌ Não   | ⚠️ Parcial| Listas grandes com bom pivô              |
| **Merge Sort**     | O(n log n)  | O(n log n)| O(n)          | ✅ Sim   | ❌ Não    | Listas grandes com necessidade de estabilidade |

---

## 📌 Legenda

- **Tempo Médio / Pior Caso:** comportamento conforme o tamanho da entrada aumenta.
- **Espaço Extra:** memória além da lista original.
- **Estável:** mantém a ordem de elementos iguais.
- **In-place:** não usa estruturas auxiliares grandes.
- **Uso prático:** cenário ideal de aplicação.

