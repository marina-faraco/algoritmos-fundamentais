from pilha import Pilha
from fila import Fila
from lista_encadeada import *
from deque import *
from tabela_hash import *

# ---------------------------------------------------------------

print('-' * 30)
print(f'{'PILHA':^30}')
print('-' * 30)

p = Pilha()

p.push(1)
p.push(2)
p.push(3)

print(p.pop())       # Esperado: 3
print(p.peek())      # Esperado: 2
print(p.is_empty())  # Esperado: False
p.pop()
p.pop()
print(p.is_empty())  # Esperado: True

# ---------------------------------------------------------------

print('-' * 30)
print(f'{'FILA':^30}')
print('-' * 30)

f = Fila()

f.enqueue(1)
f.enqueue(2)
f.enqueue(3)

print(f.dequeue())      # Esperado: 1
print(f.peek())         # Esperado: 2
print(f.is_empty())     # Esperado: False
f.dequeue()
f.dequeue()
print(f.is_empty())     # Esperado: True

# ---------------------------------------------------------------

print('-' * 30)
print(f'{'LISTA ENCADEADA':^30}')
print('-' * 30)

l = Lista_encadeada()

l.insert(1)
l.insert(2)
l.insert(3)

l.exibir()             # Esperado: 3 2 1

print(l.search(2))     # Esperado: 2
print(l.search(5))     # Esperado: None
print(l.is_empty())    # Esperado: False

l.delete(2)
l.exibir()             # Esperado: 3 1

l.delete(3)
l.delete(1)
print(l.is_empty())    # Esperado: True

# ---------------------------------------------------------------

print('-' * 30)
print(f'{'DEQUE':^30}')
print('-' * 30)

d = Deque()

d.append_left(2)
d.append_left(1)
d.append_right(3)

print(d.pop_left())         # Esperado: 1

print(d.peek_left())        # Esperado: 2
print(d.peek_right())       # Esperado: 3

print(d.pop_right())        # Esperado: 3

print(d.is_empty())         # Esperado: False

d.pop_left()

print(d.is_empty())         # Esperado: True

# ---------------------------------------------------------------

print('-' * 30)
print(f'{'TABELA HASH':^30}')
print('-' * 30)

t = TabelaHash(10)

t.inserir("nome", "Mah")
t.inserir("idade", 20)

print(t.get("nome"))    # Mah
print(t.get("idade"))   # 20

t.delete("idade")
print(t.get("idade"))   # Erro! Chave não encontrada

print(t.is_empty())     # False