class Encadeado:
    def __init__(self, nome):
        self.nome = nome
        self.next = None
        self.visitado = False

def add(v, origem, destino):
    if v[origem] == '':
        v[origem] = Encadeado(destino)
    else:
        temp = Encadeado(destino)
        temp.next = v[origem]
        v[origem] = temp

def dfs(v, i,):
    v[i].visitado = True
    temp = v[i]
    v[0] += [i]
    while temp != None:
        if v[temp.nome].visitado == False:
            dfs(v, temp.nome)
        temp = temp.next
    

def main():
    n, m = input().split()
    n, m = int(n), int(m)
    V = [[]] + [''] * n
    for _ in range(m):
        origem, destino = input().split()
        origem, destino = int(origem), int(destino)
        add(V,origem, destino)
        add(V,destino, origem)
    
    for i in range(1,n):
        if V[i] != '':
            dfs(V, i)
        else:
            V[0] += [i]
        print(len(V[0]), end=' ')
        for j in range(len(V[0])):
            k = V[0][j]
            if V[k] != '':
                V[k].visitado = False
        V[0] = []
    if V[n] != '':
        dfs(V, n)
    else:
        V[0] += [n]
    print(len(V[0]))


if __name__ == '__main__':
    main()
