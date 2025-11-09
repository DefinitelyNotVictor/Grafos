# Grafos
Por: José Neto (RA 1994079) | Lucas Gabriel (RA 1996558) | Victor Gaspareto (2018051)

# Implementação de Grafo em Python

Este é um programa que implementa um grafo não direcionado utilizando Python. O grafo é representado através de um dicionário onde cada vértice é uma chave e seus vizinhos são armazenados em uma lista.

## Funcionalidades

O programa oferece as seguintes operações:

1. **Visualização do Grafo**: Exibe a estrutura atual do grafo
2. **Inserção de Vértices**: Adiciona novos vértices ao grafo
3. **Inserção de Arestas**: Cria conexões entre vértices
4. **Remoção de Vértices**: Remove vértices e suas conexões
5. **Remoção de Arestas**: Remove conexões entre vértices
6. **Listagem de Vizinhos**: Mostra todos os vértices conectados a um vértice específico
7. **Verificação de Arestas**: Verifica se existe conexão entre dois vértices
8. **Cálculo de Grau**: Calcula o grau de todos os vértices
9. **Verificação de Percurso**: Verifica se um caminho é válido no grafo

## Como Usar

1. Execute o arquivo `main.py`
2. Use o menu interativo para realizar operações no grafo
3. Digite `0` para sair do programa

## Estrutura do Código

- `criar_grafo()`: Inicializa um novo grafo vazio
- `inserir_vertice(grafo, vertice)`: Adiciona um novo vértice ao grafo
- `inserir_aresta(grafo, origem, destino, nao_direcionado=True)`: Cria uma aresta entre dois vértices
- `vizinhos(grafo, vertice)`: Retorna a lista de vizinhos de um vértice
- `listar_vizinhos(grafo, vertice)`: Exibe os vizinhos de um vértice
- `exibir_grafo(grafo)`: Mostra a estrutura completa do grafo
- `remover_aresta(grafo, origem, destino, nao_direcionado=True)`: Remove uma aresta entre dois vértices
- `remover_vertice(grafo, vertice, nao_direcionado=True)`: Remove um vértice e todas suas conexões
- `existe_aresta(grafo, origem, destino)`: Verifica a existência de uma aresta
- `grau_vertices(grafo)`: Calcula e exibe o grau de cada vértice
- `percurso_valido(grafo, caminho)`: Verifica se um caminho é válido no grafo

## Exemplo de Uso

```python
grafo = criar_grafo()
inserir_vertice(grafo, "A")
inserir_vertice(grafo, "B")
inserir_aresta(grafo, "A", "B")
listar_vizinhos(grafo, "A")  # Mostrará B como vizinho de A
Observações
O grafo é implementado como não direcionado por padrão
Operações inválidas (como inserir vértices duplicados) são tratadas com mensagens de erro apropriadas
O programa continuará executando até que o usuário escolha a opção de sair
