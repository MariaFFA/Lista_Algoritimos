class Encadeado:
    def __init__(self, nome):
        self.nome = nome
        self.next = None

def position(name, M):
    soma = 0
    for i in range(len(name)):
        soma += ord(name[i]) * (i+1)
    posicao = (soma * 17 ) % M
    return posicao

def post(nome, M):
    posicao = position(nome, len(M))
    nome = Encadeado(nome)
    if not M[posicao]:
        M[posicao] = nome
    else:
        nome.next = M[posicao]
        M[posicao] = nome

def get(nome, M):
    posicao = position(nome, len(M))
    if not M[posicao]:
        print('404 - NOT FOUND')
    elif M[posicao].nome == nome:
        print(str(posicao), '1')
    else:
        j = 2
        first = M[posicao]
        while first.next.nome != nome:
            first = first.next
            j += 1
        print(str(posicao), str(j))

def delete(nome, M):
    posicao = position(nome, len(M))
    first = M[posicao]
    if first and first.nome == nome:
        M[posicao] = first.next
        print('DELETADO')
    elif first:
        while first.next and first.next.nome != nome:
            first = first.next
        if first.next:
            first.next = first.next.next
            print('DELETADO')

def main():
    MC = input()
    MC = MC.split(' ')
    M, C = int(MC[0]), int(MC[1])
    M = ['']*M
    for _ in range(C):
        post_nome = input()
        post_nome = post_nome.split(' ')
        nome = post_nome[1]
        post(nome, M)
    N = int(input())
    for __ in range(N):
        acao_nome = input()
        acao_nome = acao_nome.split(' ')
        acao, nome = acao_nome[0], acao_nome[1]
        if acao == 'POST':
            post(nome, M)
        elif acao == 'GET':
            get(nome, M)
        else:
            delete(nome,M)

if __name__ == '__main__':
    main()
