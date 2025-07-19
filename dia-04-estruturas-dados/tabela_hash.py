# Classe da Tabela Hash
class TabelaHash:
    def __init__(self, t):
        self.tamanho = t    
        self.tabela = [None] * t    # Cria a estrutura base com tamanho fixo

    # Função hash simplificada
    def funcao_hash(self, chave):
        return hash(chave) % self.tamanho   # Converte a chave em um índice válido
    
    # Adiciona ou atualiza elementos na tabela
    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)   # Calcula o índice com a função hash 

        if self.tabela[indice] is None:
            self.tabela[indice] = []   # Cria uma lista vazia se a posição estiver nula
        
        # verifica se a chave já existe, e atualiza o valor
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                self.tabela[indice][i] = (chave, valor)    # Atualiza o par existente
                return

        # Se a chave não existir, adiciona novo par
        self.tabela[indice].append((chave, valor)) 

    # Busca um valor pela chave
    def get(self, chave):
        indice = self.funcao_hash(chave)

        if self.tabela[indice] is None:
            return 'Erro! Tabela vazia'
        
        # Percorre a lista daquele índice para buscar a chave
        for (k, v) in self.tabela[indice]:
            if k == chave:
                return v
        
        return 'Erro! Chave não encontrada'
    
    # Remove um par (chave, valor) da tabela 
    def delete(self, chave):
        indice = self.funcao_hash(chave)

        if self.tabela[indice] is None:
            return 'Erro! Tabela vazia'
        
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                del self.tabela[indice][i]
                return 'Item removido'
        
        return 'Chave não encontrada'
        
    # Verifica se a tabela está vazia (todas as posições são None ou listas vazias)
    def is_empty(self):
        for slot in self.tabela:
            if slot:  # Se for uma lista com itens
                return False
        return True
        