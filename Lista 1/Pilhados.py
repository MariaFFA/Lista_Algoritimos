def paridade_igual(n_cima,n_baixo):
    subtracao = n_cima - n_baixo
    if subtracao%2 == 0:
        n_novo = int(((subtracao)**2)**(1/2))
    else: 
        n_novo = None
    return n_novo

def main():
    t = int(input())
    espaco = input()
    rodada = 1
    while rodada <= t:
        pilha = ['']
        caixa = int(input())
        index = -1
        while caixa != 0:
            index += 1
            try:
                pilha[index] = caixa
            except:
                pilha *= 2
                pilha[index] = caixa
            if index > 0:
                top = paridade_igual(pilha[index],pilha[index-1])
                if top != None:
                    index -=1
                    pilha[index] = top
            caixa = int(input())
        espaco = input()
        if index == -1:
            top = -1
        else:
            top = pilha[index]
        print('Pilha ',rodada,': ',(index+1), ' ', top, sep='')
        rodada += 1    

if __name__ == '__main__':
    main()
