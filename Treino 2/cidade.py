'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade,
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a
letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.

ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
'''

def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d[0] not in dist:
                orla.add(d[0])
                dist[d[0]] = float("inf")
            index = adj[v].index(d)
            if dist[v] + adj[v][index][1] < dist[d[0]]:
                dist[d[0]] = dist[v] + adj[v][index][1]
    return dist


def tamanho(ruas):
    adj = {}

    for rua in ruas:
        if rua[0] not in adj:
            adj[rua[0]] = []

        if rua[-1] not in adj:
            adj[rua[-1]] = []

        if rua[0] != rua[-1]:
            adj[rua[0]].append((rua[-1],len(rua)))
            adj[rua[-1]].append((rua[0],len(rua)))
        else:
            adj[rua[0]].append((rua[-1],0))
            adj[rua[-1]].append((rua[0],0))

    print(adj)

    biggest = 0
    for rua in adj:
        maior = max(list(dijkstra(adj,rua).values()))
        print(maior)
        if maior > biggest:
            biggest = maior

    return biggest

