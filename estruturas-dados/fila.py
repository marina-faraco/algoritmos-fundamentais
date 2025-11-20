# Classe fila
class Fila:
    def __init__(self):
        self.itens = []

    # Adiciona elementos ao final da fila
    def enqueue(self, valor):
        self.itens.append(valor)

    # Remove um elemento do inicio da lista
    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)    # 0 corresponde ao índice zero
                
    # Retorna o 1° elemento da lista
    def peek(self):
        if not self.is_empty():        
            return self.itens[0]

    # Checa se a lista está vazia
    def is_empty(self):
        return len(self.itens) == 0
