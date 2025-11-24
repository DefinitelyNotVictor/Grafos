def Busca_Profundidade_ciclo(grafo, vertice, visitados, loop_pilha):
    loop_pilha.add(vertice)
    
    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            if Busca_Profundidade_ciclo(grafo, vizinho, visitados, loop_pilha):
                return True
        elif vizinho in loop_pilha:
            return True
    
    loop_pilha.remove(vertice)
    visitados.add(vertice)
    
    return False

def tem_ciclo(grafo):
    visitados = set()
    loop_pilha = set()

    for vertice in grafo:
        if vertice not in visitados:
            if Busca_Profundidade_ciclo(grafo, vertice, visitados, loop_pilha):
                return True
    return False

# Exemplo

grafo = {
    0: [1],
    1: [2],
    2: [0],
    3: [4],
    4: [5],
    5: []  # Sem ciclo
}

if tem_ciclo(grafo):
    print("Tem ciclo")
else:
    print("Não tem ciclo")
