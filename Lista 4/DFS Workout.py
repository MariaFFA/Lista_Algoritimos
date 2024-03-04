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

def dfs(v, i):
    v[i].visitado = True
    print(i, end=' ')
    temp = v[i]
    while temp != None:
        if v[temp.nome].visitado == False:
            dfs(v, temp.nome)
        temp = temp.next

def main():
    vertices = int(input())
    V = [''] * vertices
    fim = 1
    while fim != 0:
        origem, destino, fim = input().split()
        origem, destino, fim = int(origem), int(destino), int(fim)
        add(V,origem, destino)
        add(V,destino, origem)
    
    for i in range(vertices):
        print(i, end=': ')
        if V[i] == '':
            print('Lista Vazia')
        else:
            temp = V[i]
            while temp != None:
                print(temp.nome, end=' ')
                temp = temp.next
            print()
    print()

    dfs(V, 0)


if __name__ == '__main__':
    main()
