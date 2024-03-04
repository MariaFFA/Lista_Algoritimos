def floyd_warshall(graph):
    n = len(graph)
    dist = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def update_dist(dist, q, a, b, m):
    if dist[a][b] > m:
        dist[a][b] = m
        for i in range(q):
            for j in range(q):
                if dist[i][j] > dist[i][a] + dist[a][b] + dist[b][j]:
                    dist[i][j] = dist[i][a] + dist[a][b] + dist[b][j]
                    update_dist(dist, q, i, j, dist[i][j])
    return dist

def main():
    q, r, n = input().split(' ')
    q, r, n = int(q), int(r), int(n)
    Q = ['']*q
    for i in range(q):
        Q[i] = [float("inf")]*q
        Q[i][i] = 0
    for i in range(r):
        a, b, m = input().split(' ')
        a, b, m = int(a), int(b), int(m)
        Q[a][b] = m
    dist = floyd_warshall(Q)

    for i in range(n):
        evento = input().split(' ')
        if evento[0] == '1':
            a, b, m = int(evento[1]), int(evento[2]), int(evento[3])
            update_dist(dist, q, a, b, m)
        else:
            a, b = int(evento[1]), int(evento[2])
            if a == b:
                print(0)
            else:
                tempo_total = dist[a][b]
                if tempo_total == float("inf"):
                    print(-1)
                else:
                    print(tempo_total)


if __name__ == '__main__':
    main()
