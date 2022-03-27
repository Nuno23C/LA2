'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''

def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]

    return dist


def viagem(rotas,o,d):
    adj = {}

    if o == d:
        return 0

    for rota in rotas:
        i = 0
        while i < len(rota)-1:
            if rota[i] not in adj:
                adj[rota[i]] = {}

            if rota[i+2] not in adj:
                adj[rota[i+2]] = {}

            adj[rota[i]][rota[i+2]] = rota[i+1]
            adj[rota[i+2]][rota[i]] = rota[i+1]

            i+= 2

    print(adj)

    dist = dijkstra(adj, o)

    print(dist)

    return dist[d]
