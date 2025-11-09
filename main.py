def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print(f"O vértice {vertice} já existe no grafo.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=True):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        print(f"O vértice {vertice} não existe no grafo.")
        return []


def listar_vizinhos(grafo, vertice):
    if vertice not in grafo:
        print(f"O vértice {vertice} não existe no grafo.")
    else:
        lista = vizinhos(grafo, vertice)
        print(f"Vizinhos do vértice {vertice}: {lista}")


def exibir_grafo(grafo):
    for vertice in grafo:
        print(f"{vertice} -> {grafo[vertice]}")


def remover_aresta(grafo, origem, destino, nao_direcionado=True):
    if origem not in grafo or destino not in grafo:
        print("Um dos vértices não existe!")
        return

    if destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"O vértice {vertice} não existe no grafo.")
        return

    for v in list(grafo.keys()):
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

    del grafo[vertice]


def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        return True
    return False


def grau_vertices(grafo):
    graus = {}
    for v in grafo:
        graus[v] = len(grafo[v])
    print("Grau de cada vértice:")
    for v, g in graus.items():
        print(f"{v}: {g}")
    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


def main():
    grafo = criar_grafo()

    while True:
        print("\n--- MENU ---")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos de um vértice")
        print("7 - Verificar existência de aresta")
        print("8 - Calcular grau dos vértices")
        print("9 - Verificar percurso")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_grafo(grafo)
        elif opcao == "2":
            v = input("Digite o nome do vértice: ")
            inserir_vertice(grafo, v)
        elif opcao == "3":
            o = input("Vértice de origem: ")
            d = input("Vértice de destino: ")
            inserir_aresta(grafo, o, d, nao_direcionado=True)
        elif opcao == "4":
            v = input("Digite o vértice a ser removido: ")
            remover_vertice(grafo, v)
        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            remover_aresta(grafo, o, d, nao_direcionado=True)
        elif opcao == "6":
            v = input("Digite o vértice: ")
            listar_vizinhos(grafo, v)
        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(grafo, o, d))
        elif opcao == "8":
            grau_vertices(grafo)
        elif opcao == "9":
            caminho = input("Digite o percurso (ex: A B C): ").split()
            print("Percurso válido?", percurso_valido(grafo, caminho))
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
