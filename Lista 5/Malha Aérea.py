class Peso:
    def __init__(self, peso, origem, destino):
        self.peso = peso
        self.origem = origem
        self.destino = destino

class Encadeado:
    def __init__(self, nome, peso):
        self.nome = nome
        self.next = None
        self.visitado = False
        self.peso = peso

def add(v, origem, destino, peso):
    if v[origem] == '':
        v[origem] = Encadeado(destino, peso)
    else:
        temp = Encadeado(destino, peso)
        temp.next = v[origem]
        v[origem] = temp

def prim(v, visitados, min_edges, e, grupos, soma = 0):
    origem, destino = min_edges[e].origem, min_edges[e].destino
    if grupos[origem] == '' and grupos[destino] == '':
        grupos[origem] = origem
        grupos[destino] = origem
    elif grupos[origem] == '' and grupos[destino] != '':
        grupos[origem] = grupos[destino]
    elif grupos[origem] != '' and grupos[destino] == '':
        grupos[destino] = grupos[origem]
    else:
        destino = grupos[destino]
        for i in range(len(grupos)):
            if grupos[i] == destino:
                grupos[i] = grupos[origem]
    visitados[origem] = True
    visitados[destino] = True
    soma += min_edges[e].peso
    if False in visitados:
        while grupos[min_edges[e].origem] == grupos[min_edges[e].destino] and grupos[min_edges[e].origem] != '':
            e += 1
        prim(v, visitados, min_edges, e, grupos, soma)
    else:
        print(soma)

def build_max_heap(v):
    for i in range(len(v)//2, -1, -1):
        max_heapify(v, i)

def heap_sort(v):
    build_max_heap(v)
    for i in range(len(v) - 1, 0, -1):
        v[i], v[0] = v[0], v[i]
        v_heap = v[:i]
        max_heapify(v_heap, 0)
        v[:i] = v_heap 
    return v

def max_heapify(v, i):
    l = i*2 + 1
    r = i*2 + 2
    if l < len(v) and (v[l].peso > v[i].peso or (v[l].peso == v[i].peso and v[l].origem > v[i].origem) or (v[l].peso == v[i].peso and v[l].origem == v[i].origem and v[l].destino > v[i].destino)):
        maior = l
    else:
        maior = i
    if r < len(v) and (v[r].peso > v[maior].peso or (v[r].peso == v[maior].peso and v[r].origem > v[maior].origem) or (v[r].peso == v[maior].peso and v[r].origem == v[maior].origem and v[r].destino > v[maior].destino)):
        maior = r
    if maior != i:
        v[i], v[maior] = v[maior], v[i]
        max_heapify(v, maior)

def main():
    n, m = input().split()
    n, m = int(n), int(m)
    V = [''] * n
    min_edges = [float("inf")] * m
    grupos = [''] * n
    for _ in range(m):
        origem, destino, peso = input().split()
        origem, destino, peso = int(origem), int(destino), int(peso)
        add(V,origem, destino, peso)
        min_edges[_] = Peso(peso, origem, destino)
    min_edges = heap_sort(min_edges)
    prim(V, [False]*n, min_edges, 0, grupos)


if __name__ == '__main__':
    main()
