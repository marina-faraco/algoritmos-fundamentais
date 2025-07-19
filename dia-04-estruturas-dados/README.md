# Estruturas de dados

## Pilhas 
A pilha funciona recursivamente. Seguindo o que chamamos de LIFO (last In, First Out), ou seja, o último elemento adicionado a lista será o primeiro 'lido'. Portanto, as pilhas funcionam adicionando e retirando elementos do final.

**Vantagem:** A pilha controla a ordem de chamada de funções. Ou seja, quando uma função é chamada dentro de outro (recursão), é a pilha de chamada que determina o momento de entrar e sair de cada função.

**Desvantagem:** Em pilhas muito grandes utiliza-se muita memória, o que pode levar a um erro de Overflow. E não é possível acessar elementos de forma aleatório.

## Fila
As filas possuem funcionamento similar ao das pilhas. No entanto, as filas são estruturas de dados FIFO (First In, First Out). Portanto funcionam adicionando elementos no final e removendo do início.

**Vantagem:** Permite a pesquisa de elementos seguindo a ordem em que foram adicionados.

**Desvantagens:** Não é possiível acessar elementos de forma aleatória.

## Lista Encadeada
Listas encadeadas permitem armazenar listas de elementos na memória. Quando se trata de arrays, sabemos que os elementos são armezenados de forma contigua. Já em listas encadeadas cada item armazena o endereço do próximo item. Assim, conectando endereços aleatórios da memória.

**Vantagens:** 

**Desvantagens:** Não é possível acessar elemetos aleatóriamente. Para encontar um item é necessário percorrer toda a lista.

# Deque
Como já mencionado anteriormente, pilhas são estruturas de dados LIFO (Last In, First Out) e filas são estruturas FIFO (First In, First Out). Deques são estruturas de dados que seguem um funcionamento semelhante ao de pilhas e filas. Porém, diferenciam-se por possibilitarem a manipulação de dados em ambas as direções (tanto pelo começo, quanto pelo final). Ou seja, permitem adicionar e remover itens tanto do início quando do final.

**Vantagens:**

**Desvantagens:**

# Tabela Hash
Tabela hash é uma estrutura de dados que armazena informações associando chaves a valores, permitindo buscar, inserir e remover elementos de forma muito rápida. Ela funciona aplicando uma função hash sobre a chave para determinar onde o valor será armazenado. Ou seja, é uma forma eficiente de implementar um dicionário.

**Vantagens:** Seu tempo de exucução é O(1), e O(n) no pior caso.

**Desvantagens:**