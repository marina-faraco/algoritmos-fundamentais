# 📘 Busca Linear

## 🔍 O que é?

A **busca linear** (ou **busca sequencial**) é um dos algoritmos mais simples para localizar um valor dentro de uma lista. Ela verifica **elemento por elemento**, do início ao fim, até encontrar o valor desejado — ou concluir que ele não está presente.

### 🧠 Complexidade de tempo: **O(n)**  
Isso significa que o tempo de execução **cresce proporcionalmente** ao número de elementos da lista.  
Exemplos:
- Lista com 10 elementos → **O(10)**
- Lista com 20 elementos → **O(20)**
- Lista com 1.000.000 de elementos → **O(1.000.000)** → **ineficiente em listas grandes**

> 🟢 Em listas pequenas, isso não é um problema.  
> 🔴 Em listas muito grandes, pode ser lento e inviável.

### 🕑 Variação do tempo conforme a posição do elemento:
- **Melhor caso (O(1))**: o valor está no início da lista.
- **Pior caso (O(n))**: o valor está no fim ou não está presente.
- **Espaço de memória**: **O(1)** → não usa memória extra significativa.

---

## ⚙️ Como funciona?

1. Começa do primeiro elemento.
2. Compara cada item com o **valor alvo**.
3. Se encontrar, retorna a **posição**.
4. Se chegar ao final sem encontrar, retorna que **não existe**.

---

## ✅ Exemplos de uso

- Procurar o **nome de um usuário** em uma lista.
- Verificar se uma **palavra** aparece em um texto.
- Checar se um número **existe em uma sequência** de dados.

---

## 🧪 Execução

**python**

    lista = [10, 20, 30, 40]
    alvo = 30

    # Saída esperada:
    # Valor encontrado na posição 2
