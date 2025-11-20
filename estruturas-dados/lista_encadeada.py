# Classe que representa um nó na lista
class No:
    def __init__(self, valor):
        self.valor = valor      # Valor armazenado no nó
        self.proximo = None     # Referência para o próximo nó da lista (inicialmente nula)

# Classe que representa a lista encadeada
class Lista_encadeada:
    def __init__(self):
        self.head = None    # Início da lista (nó cabeça), inicialmente vazia

    # Adiciona um elemento no inicio da lista
    def insert(self, valor):
        novo_No = No(valor)             # Criar um novo nó 
        novo_No.proximo = self.head     # Conecta a um nó já existente
        self.head = novo_No             # Atualiza o head

    # Remove o primeiro nó da lista com o valor especificado
    def delete(self, valor):
        no_atual = self.head            # Começa pelo início da lista
        no_anterior = None              # Inicialmente, não há nó anterior

        # Percorre a lista até encontrar o valor ou o final
        while no_atual is not None:
            if no_atual.valor == valor:     # Valor encontrado
                if no_anterior is None:     # Caso especial: o valor está no head
                    self.head = no_atual.proximo
                else:
                    no_anterior.proximo = no_atual.proximo  # Pula o nó atual
                
                return  # Interrompe após deletar
            no_anterior = no_atual
            no_atual = no_atual.proximo      

    # Procura por um elemento na lista
    def search(self, valor):
        no_atual = self.head
        while no_atual is not None:
            if no_atual.valor == valor:
                return no_atual.valor
            no_atual = no_atual.proximo
        
        return None

    # Imprime todos os valores da lista
    def exibir(self):
        no_atual = self.head
        while no_atual is not None:
            print(no_atual.valor)
            no_atual = no_atual.proximo

    # Verifica se a lista está vazia
    def is_empty(self):
        return self.head == None




