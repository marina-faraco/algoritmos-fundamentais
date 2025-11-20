# Classe Deque
class Deque:
    def __init__(self):
        self.itens = []

    # Adiciona elemento no início
    def append_left(self, valor):
        self.itens.insert(0, valor)

    # Adiciona elemento no final
    def append_right(self, valor):
        self.itens.append(valor)

    # Remove elemento do início
    def pop_left(self):
        if not self.is_empty():
            return self.itens.pop(0)
        return None

    # Remove elemento do final
    def pop_right(self):
        if not self.is_empty():
            return self.itens.pop()
        return None

    # Retorna elemento do início
    def peek_left(self):
        if not self.is_empty():
            return self.itens[0]
        return None

    # retorna elemento do final
    def peek_right(self):
        if not self.is_empty():
            return self.itens[-1]
        return None

    # Verifica se a lista está vazia
    def is_empty(self):
        return len(self.itens) == 0
    

