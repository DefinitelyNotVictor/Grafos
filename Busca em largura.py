from collections import deque

class Grafo:

    def __init__(self):

        self.adj = {}

    def adicionar_aresta(self, u, v, bidirecional=True):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append(v)
        if bidirecional:
            self.adj[v].append(u)
    
    def busca_em_largura(self, inicio):
        if inicio not in self.adj:
            print(f"Erro: Nó de início '{inicio}' não encontrado no grafo.")
            return set(), {}

        fila = deque([inicio])
        
        visitados = {inicio}
        
        distancia = {n: -1 for n in self.adj}
        distancia[inicio] = 0

        print(f"Iniciando BFS a partir do nó: {inicio}")
        
        while fila:
            u = fila.popleft()
            print(f"Visitando nó: {u} (Distância: {distancia[u]})")

            for v in self.adj.get(u, []):
                if v not in visitados:
                    visitados.add(v)
                    distancia[v] = distancia[u] + 1
                    fila.append(v)
        
        return visitados, distancia

    def bfs_menor_caminho(self, inicio, alvo):
        if inicio not in self.adj or alvo not in self.adj:
            print("Erro: Nós de início ou alvo não encontrados no grafo.")
            return None

        fila = deque([inicio])
        visitados = {inicio}
        
        pai = {n: None for n in self.adj}
        
        caminho_encontrado = False

        while fila:
            u = fila.popleft()

            if u == alvo:
                caminho_encontrado = True
                break

            for v in self.adj.get(u, []):
                if v not in visitados:
                    visitados.add(v)
                    pai[v] = u
                    fila.append(v)

        if not caminho_encontrado:
            print(f"Não foi encontrado um caminho de {inicio} para {alvo}.")
            return None
        
        caminho = []
        no_atual = alvo
        while no_atual is not None:
            caminho.append(no_atual)
            no_atual = pai.get(no_atual)
        
        caminho.reverse() 
        return caminho