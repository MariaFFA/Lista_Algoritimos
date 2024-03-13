class Encadeado:
    def __init__(self, nome):
        self.nome = nome
        self.next = None

def remove_paredes(p, paredes_x, paredes_y):
    linha = p // (2*len(paredes_y)-1)
    if p % (2*len(paredes_y)-1) < len(paredes_y)-1:
        coluna = p % (2*len(paredes_y)-1)
        paredes_y[linha][coluna] = False
    else:
        coluna = p % (2*len(paredes_y)-1) - len(paredes_y) + 1
        paredes_x[linha][coluna] = False

def conectados(a, b, paredes_x, paredes_y, celulas):
    linha_a = a // (len(celulas))
    coluna_a = a % (len(celulas))
    linha_b = b // (len(celulas))
    coluna_b = b % (len(celulas))
    if celulas[linha_a][coluna_a] != '' and celulas[linha_b][coluna_b] != '':
        if celulas[linha_a][coluna_a] == celulas[linha_b][coluna_b]:
            return '1', celulas
        else:
            return '0', celulas
    elif celulas[linha_a][coluna_a] != '' or celulas[linha_b][coluna_b] != '':
        return '0', celulas
    celulas = uniao(a,Encadeado((linha_a, coluna_a)), paredes_x, paredes_y, celulas)
    if celulas[linha_a][coluna_a] != '' and celulas[linha_b][coluna_b] != '':
        if celulas[linha_a][coluna_a] == celulas[linha_b][coluna_b] and celulas[linha_a][coluna_a] == a:
            return '1', celulas
        else:
            return '0', celulas
    else:
        return '0', celulas

def uniao(x, pontas, paredes_x, paredes_y, matriz):
    ultimo = pontas
    ultimo_passo = pontas
    matriz[pontas.nome[0]][pontas.nome[1]] = x
    while pontas != None:
        posicion = pontas.nome
        if posicion[0] > 0 and not paredes_x[posicion[0]-1][posicion[1]] and matriz[posicion[0]-1][posicion[1]] == '':
            matriz[posicion[0]-1][posicion[1]] = x
            pontas, ultimo = add_pontas(pontas, (posicion[0]-1, posicion[1]), ultimo)
        if posicion[0] < len(matriz)-1 and not paredes_x[posicion[0]][posicion[1]] and matriz[posicion[0]+1][posicion[1]] == '':
            matriz[posicion[0]+1][posicion[1]] = x
            pontas, ultimo = add_pontas(pontas, (posicion[0]+1, posicion[1]), ultimo)
        if posicion[1] > 0 and not paredes_y[posicion[0]][posicion[1]-1] and matriz[posicion[0]][posicion[1]-1] == '':
            matriz[posicion[0]][posicion[1]-1] = x
            pontas, ultimo = add_pontas(pontas, (posicion[0], posicion[1]-1), ultimo)
        if posicion[1] < len(matriz[0])-1 and not paredes_y[posicion[0]][posicion[1]] and matriz[posicion[0]][posicion[1]+1] == '':
            matriz[posicion[0]][posicion[1]+1] = x
            pontas, ultimo = add_pontas(pontas, (posicion[0], posicion[1]+1), ultimo)
        if posicion == ultimo_passo:
            ultimo_passo = ultimo
        pontas = pontas.next
    matriz[posicion[0]][posicion[1]] = x
    return matriz


def add_pontas(pontas, add, ultimo):
    ultimo.next = Encadeado(add)
    return pontas, ultimo.next

def main():
    k = int(input())
    for l in range(k):
        n, m, q = input().split(' ')
        n, m, q = int(n), int(m), int(q)
        paredes_x = [[]] * (n-1)
        for i in range(n-1):
            paredes_x[i] = [True] * (n)
        paredes_y = [[]] * (n)
        for i in range(n):
            paredes_y[i] = [True] * (n-1)
        celulas = [[]]*n
        for i in range(n):
            celulas[i] = ['']*n
        for _ in range(m):
            p = int(input())
            remove_paredes(p, paredes_x, paredes_y)
        for c in range(q):
            a, b = input().split(' ')
            a, b = int(a), int(b)
            resultado, celulas = conectados(a, b, paredes_x, paredes_y, celulas)
            print(str(l) + '.' + str(c) + ' ' + resultado, sep='')
        z = input()
        print()

if __name__ == '__main__':
    main()