def main():
    entrada = input()
    total = 0
    formulada = True
    for i in entrada:
        if i == '{':
            total += 1
        elif i == '}':
            total -= 1
        if total < 0:
            formulada = False
    if formulada and total == 0:
        print('S')
    else: 
        print('N')


if __name__ == '__main__':
    main()
