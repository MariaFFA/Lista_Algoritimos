class Encadeado:
    def __init__(self, nome):
        self.nome = nome
        self.next = None

def percorrer(matriz, end, passos, pontas):
    ultimo = pontas
    ultimo_passo = pontas
    while pontas != None:
        posicion = pontas.nome
        if posicion == end:
            return print(passos)
        if posicion[0] > 0 and matriz[posicion[0]-1][posicion[1]] != '1':
            matriz[posicion[0]-1][posicion[1]] = '1'
            pontas, ultimo = add_pontas(pontas, (posicion[0]-1, posicion[1]), ultimo)
        if posicion[0] < len(matriz)-1 and matriz[posicion[0]+1][posicion[1]] != '1':
            matriz[posicion[0]+1][posicion[1]] = '1'
            pontas, ultimo = add_pontas(pontas, (posicion[0]+1, posicion[1]), ultimo)
        if posicion[1] > 0 and matriz[posicion[0]][posicion[1]-1] != '1':
            matriz[posicion[0]][posicion[1]-1] = '1'
            pontas, ultimo = add_pontas(pontas, (posicion[0], posicion[1]-1), ultimo)
        if posicion[1] < len(matriz[0])-1 and matriz[posicion[0]][posicion[1]+1] != '1':
            matriz[posicion[0]][posicion[1]+1] = '1'
            pontas, ultimo = add_pontas(pontas, (posicion[0], posicion[1]+1), ultimo)
        if posicion == ultimo_passo.nome:
            passos += 1
            ultimo_passo = ultimo
        pontas = pontas.next
    return print("Labirinto Impossivel")

def add_pontas(pontas, add, ultimo):
    ultimo.next = Encadeado(add)
    return pontas, ultimo.next

def main():
    linha, coluna = input().split(' ')
    linha, coluna = int(linha), int(coluna)
    matriz = [''] * linha
    start, end = None, None
    for i in range(linha):
        matriz[i] = input().split(' ')
        for j in range(coluna):
            if matriz[i][j] == '2':
                start = (i, j)
            elif matriz[i][j] == '3':
                end = (i, j)
    ponta = Encadeado(start)
    percorrer(matriz, end, 0, ponta)

if __name__ == '__main__':
    main()
