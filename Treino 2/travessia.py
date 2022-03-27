'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

mapa = ["4563",
        "9254",
        "7234",
        "3231",
        "3881"]

'''

def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]

    return dist


def verifica(mapa,x,y):
    return (0 <= x < len(mapa[0])) and (0 <= y < len(mapa))


def travessia(mapa):
    adj = {}

    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if (x,y) not in adj:
                adj[(x,y)] = {}

            if verifica(mapa,x+1,y) and (abs(int(mapa[y][x]) - int(mapa[y][x+1])) <= 2):
                    adj[(x,y)][(x+1,y)] = 1 + abs(int(mapa[y][x]) - int(mapa[y][x+1]))

            if verifica(mapa,x-1,y) and (abs(int(mapa[y][x]) - int(mapa[y][x-1])) <= 2):
                    adj[(x,y)][(x-1,y)] = 1 + abs(int(mapa[y][x]) - int(mapa[y][x-1]))

            if verifica(mapa,x,y-1) and (abs(int(mapa[y][x]) - int(mapa[y-1][x])) <= 2):
                    adj[(x,y)][(x,y-1)] = 1 + abs(int(mapa[y][x]) - int(mapa[y-1][x]))

            if verifica(mapa,x,y+1) and (abs(int(mapa[y][x]) - int(mapa[y+1][x])) <= 2):
                    adj[(x,y)][(x,y+1)] = 1 + abs(int(mapa[y][x]) - int(mapa[y+1][x]))

    print(adj)

    dists = []
    for pos_i in range(len(mapa[0])):
        custos = dijkstra(adj,(pos_i,0))
        for pos_f in range(len(mapa[0])):
            if (pos_f,len(mapa)-1) in custos:
                dists.append((pos_i, custos[(pos_f,len(mapa)-1)]))

    dists.sort(key = lambda x: (x[1],x[0]))

    print(dists)

    return dists[0]
