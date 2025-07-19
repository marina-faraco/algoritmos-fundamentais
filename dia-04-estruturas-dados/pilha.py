# classe pilha 
class Pilha:
    def __init__(self):
        self.itens = []

    # adiciona elementos ao topo da pilha 
    def push(self, valor):
        self.itens.append(valor)

    # retira um elemento do inicio da lista
    def pop(self):
        if not self.is_empty():
            return self.itens.pop()

    # Retorna o 1° elemento da lista
    def peek(self):
        if not self.is_empty():
            return self.itens[-1]

    # checa se a lista está vazia
    def is_empty(self):
        return len(self.itens) == 0
    
    