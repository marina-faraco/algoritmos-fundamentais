# Estruturas de Dados

## Pilhas
A pilha funciona de forma semelhante a um sistema recursivo, seguindo o princípio **LIFO** (*Last In, First Out*), ou seja, o último elemento adicionado é o primeiro a ser removido. Isso significa que os elementos são adicionados e removidos sempre pelo final da estrutura.

**Vantagens:**  
- Controla a ordem de chamadas de funções, sendo essencial em processos recursivos.  
- Facilita a gestão da execução de funções aninhadas.

**Desvantagens:**  
- Em pilhas muito grandes, pode haver alto consumo de memória, levando a erros como *stack overflow*.  
- Não permite acesso aleatório aos elementos.

---

## Filas
As filas funcionam de maneira semelhante às pilhas, mas seguem o princípio **FIFO** (*First In, First Out*). Ou seja, os elementos são adicionados no final e removidos do início da estrutura.

**Vantagens:**  
- Permite o processamento dos elementos na ordem em que foram adicionados.  
- Ideal para situações como filas de impressão, buffers, agendamento de tarefas, etc.

**Desvantagens:**  
- Não permite acesso aleatório aos elementos.  
- Pode ser ineficiente se não for implementada com estrutura circular ou ponteiros.

---

## Listas Encadeadas
As listas encadeadas armazenam elementos de forma não contígua na memória. Diferente dos arrays, onde os elementos ocupam posições consecutivas, cada elemento (ou nó) da lista armazena um valor e o endereço do próximo nó, formando uma cadeia.

**Vantagens:**  
- Fácil inserção e remoção de elementos em qualquer ponto da lista.  
- Uso eficiente de memória em operações dinâmicas.

**Desvantagens:**  
- Acesso sequencial: é necessário percorrer a lista do início até o elemento desejado.  
- Maior uso de memória devido aos ponteiros adicionais.

---

## Deque
Um **Deque** (*Double Ended Queue*) é uma estrutura de dados que permite inserções e remoções tanto no início quanto no final da fila, combinando características de pilhas (LIFO) e filas (FIFO).

**Vantagens:**  
- Flexível, pois permite operações em ambas as extremidades.  
- Útil em algoritmos que exigem varredura bidirecional.

**Desvantagens:**  
- Pode ser mais complexa de implementar.  
- Pode consumir mais memória dependendo da estrutura utilizada.

---

## Tabela Hash
Uma tabela hash associa chaves a valores e permite operações de inserção, busca e remoção de forma eficiente. Utiliza uma função hash para mapear cada chave a um índice de uma tabela.

**Vantagens:**  
- Tempo de execução médio de **O(1)** para operações básicas.  
- Ideal para implementar dicionários, caches e conjuntos.

**Desvantagens:**  
- Em caso de colisão (chaves diferentes gerando o mesmo índice), o desempenho pode cair para **O(n)**.  
- A eficiência depende da qualidade da função hash.  
- Pode haver desperdício de memória.

---

> 📌 *Este é um guia introdutório sobre estruturas de dados. Para aplicações práticas e códigos de exemplo, confira os diretórios e arquivos do projeto!*
