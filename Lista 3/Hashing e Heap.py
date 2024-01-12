class Encadeado:
    def __init__(self, nome, prioridade, numero):
        self.prioridade = prioridade
        self.numero = numero
        self.nome = nome
        self.next = None
        self.fileira = None

def position(name, M):
    soma = 0
    for i in range(len(name)):
        soma += ord(name[i]) * (i+1)
    posicao = (soma * 17 ) % M
    return posicao

def post(nome,prioridade, numero, M):
    posicao = position(nome, len(M))
    nome = Encadeado(nome, prioridade, numero)
    if not M[posicao]:
        M[posicao] = nome
    else:
        nome.next = M[posicao]
        M[posicao] = nome

def delete(nome, M):
    posicao = position(nome, len(M))
    first = M[posicao]
    if first and first.nome == nome:
        M[posicao] = first.next
    elif first:
        while first.next and first.next.nome != nome:
            first = first.next
        if first.next:
            first.next = first.next.next

def max_heapify(fileira,i):
    l = i*2 + 1
    r = i*2 + 2
    if l < len(fileira) and fileira[l] and fileira[l].prioridade == fileira[i].prioridade and fileira[l].numero > fileira[i].numero:
        maior = i
    elif l < len(fileira) and fileira[l] and fileira[l].prioridade > fileira[i].prioridade:
        maior = l
    else:
        maior = i
    if r < len(fileira) and fileira[r] and fileira[r].prioridade == fileira[maior].prioridade and fileira[r].numero > fileira[i].numero:
        maior = i
    elif r < len(fileira) and fileira[r] and fileira[r].prioridade > fileira[maior].prioridade:
        maior = r
    if maior != i:
        fileira[i], fileira[maior] = fileira[maior], fileira[i]
    if i > 0:
        max_heapify(fileira,i - 1)

def min_heapify(fileira,i):
    l = i*2 + 1
    r = i*2 + 2
    if l < len(fileira) and fileira[l] and fileira[l].prioridade < fileira[i].prioridade:
        menor = l
    else:
        menor = i
    if r < len(fileira) and fileira[r] and fileira[r].prioridade < fileira[menor].prioridade:
        menor = r
    if menor != i:
        fileira[i], fileira[menor] = fileira[menor], fileira[i]
    if i > 0:
        min_heapify(fileira,i - 1)

def cadastrar(nome, prioridade, plateia, ordem, sem_assento):
    numero = Encadeado(nome,prioridade, ordem)
    for f in range(len(plateia)):
        for c in range(len(plateia[f])):
            if not plateia[f][c]:
                plateia[f][c] = numero
                numero.fileira = f+1
                print(numero.nome,' (',numero.numero,') foi alocado(a) na fileira ',numero.fileira, sep='')
                return
    lista_min = ['']*len(plateia)
    for f in range(len(plateia)):
        min_heapify(plateia[f], len(plateia[f])//2)
        lista_min[f] = plateia[f][0]
    menor = lista_min[0]
    f = 0
    for m in range(1,len(lista_min)):
        if lista_min[m].prioridade < menor.prioridade:
            menor = lista_min[m]
            f = m
    if plateia[f][0].prioridade < numero.prioridade:
        plateia[f][0].fileira = None
        add_sem_assento(sem_assento,plateia[f][0])
        numero.fileira = f+1
        plateia[f][0] = numero
        print(numero.nome,' (',numero.numero,') foi alocado(a) na fileira ',numero.fileira, sep='')
        return
    add_sem_assento(sem_assento,numero)
    print(numero.nome,' (',numero.numero,') nao foi alocado(a) em nenhuma fileira', sep='')
                
def add_sem_assento(lista, numero):
    for c in range(len(lista)):
        if not lista[c]:
            lista[c] = numero
            return
    lista += ['']*(len(lista))
    lista[len(lista)//2] = numero

def get(nome, numero, plateia, sem_assento):
    for f in range(len(plateia)):
        for c in plateia[f]:
            if c and c.nome == nome and c.numero == numero:
                return print('Sentado(a) na fileira', c.fileira)
    for c in sem_assento:
        if c and c.nome == nome and c.numero == numero:
            return print('Sem assento')
    print('Inexistente')

def remover(nome, numero, plateia, sem_assento):
    for a in range(len(sem_assento)):
        if sem_assento[a] and sem_assento[a].nome == nome and sem_assento[a].numero == numero:
            sem_assento[a] = ''
            print('Removido(a)')
            return
    for f in range(len(plateia)):
        for c in range(len(plateia[f])):
            if plateia[f][c] and plateia[f][c].nome == nome and plateia[f][c].numero == numero:
                max_heapify(sem_assento,len(sem_assento)//2)
                if not sem_assento[0]:
                    plateia[f][c] = ''
                    print('Removido(a)')
                    return
                sem_assento[0].fileira = plateia[f][c].fileira
                plateia[f][c] = sem_assento[0]
                sem_assento[0] = ''
                print('Removido(a)')        
                return
    print('Inexistente')

def rem_sem_assento(lista, numero):
    for n in range(len(lista)):
        if numero and numero.numero == lista[n].numero and numero.nome == lista[n].nome:
            lista[n] = ''
            return

def main():
    FQ = input()
    FQ = FQ.split(' ')
    F,Q = int(FQ[0]), int(FQ[1])
    plateia = ['']*F
    sem_assento = ['']
    for f in range(len(plateia)):
        plateia[f] = ['']*Q
    N = int(input())
    M = ['']*F*Q
    numero = 0
    for __ in range(N):
        acao_nome = input()
        acao_nome = acao_nome.split(' ')
        acao, nome = acao_nome[0], acao_nome[1]
        valor = int(acao_nome[2])
        if acao == 'CAD':
            numero += 1
            post(nome,valor,numero, M)
            cadastrar(nome,valor, plateia, numero, sem_assento)
        elif acao == 'REM':
            delete(nome,M)
            remover(nome,valor,plateia, sem_assento)
        else:
            get(nome, valor,plateia, sem_assento)

if __name__ == '__main__':
    main()

