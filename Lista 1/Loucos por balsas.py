def separar_informacoes(informacoes):
    primeiro = ''
    segundo = ''
    espaco = False
    for i in informacoes:
        if i == ' ':
            espaco = True
        elif not espaco:
            primeiro += i
        else:
            segundo += i
    return primeiro, segundo

def main():
    t = int(input())
    caso = 1
    while caso <= t:
        c_balsa_n_carros = input()
        c_balsa, n_carros = separar_informacoes(c_balsa_n_carros)
        c_balsa = int(c_balsa)*100
        n_carros = int(n_carros)
        lado_b = 'esquerdo'
        c_atual = 0
        travessias = 0
        carros_e = ['']*n_carros
        carros_d = ['']*n_carros
        index_e_colocar = 0
        index_d_colocar = 0
        while n_carros > 0:
            c_carro_lado_c = input()
            c_carro, lado_c = separar_informacoes(c_carro_lado_c)
            c_carro = int(c_carro)
            if lado_c == 'esquerdo':
                carros_e[index_e_colocar] = c_carro
                index_e_colocar += 1
            else:
                carros_d[index_d_colocar] = c_carro
                index_d_colocar += 1
            n_carros -= 1
        index_e = 0
        index_d = 0
        vazio = False
        while index_e + index_d < index_e_colocar + index_d_colocar:
            if lado_b == 'esquerdo':
                while index_e < index_e_colocar and c_balsa >= c_atual + carros_e[index_e]:
                    c_atual += carros_e[index_e]
                    index_e += 1
                lado_b = 'direito'
            elif lado_b == 'direito':
                while index_d < index_d_colocar and c_balsa >= c_atual + carros_d[index_d]:
                    c_atual += carros_d[index_d]
                    index_d += 1
                lado_b = 'esquerdo'
            travessias += 1
            c_atual = 0
        print('Caso ',caso,': ',travessias, sep='')
        caso += 1    

if __name__ == '__main__':
    main()
