def Busca_Profundidade(grafo, vertice, visitados = None):
    if visitados is None:
        visitados = set()
    
    visitados.add(vertice)
    print(vertice)
    
    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            Busca_Profundidade (grafo, vizinho, visitados)

# Exemplo
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Iniciar a busca em profundidade a partir do vértice 0
print("DFS a partir do vértice 0")
Busca_Profundidade(grafo, 0)
