'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra.
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si.
A função deverá devolver o tamanho do maior continente.
'''

def bfs(adj,o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return vis


def maior(vizinhos):
    if vizinhos == []:
        return 0

    ligados = {}

    for conj in vizinhos:
        for pais1 in conj:
            if pais1 not in ligados:
                ligados[pais1] = []
            for pais2 in conj:
                if pais2 != pais1:
                    ligados[pais1].append(pais2)

    max = 0
    for o in ligados:
        vis = bfs(ligados,o)
        if len(vis) > max:
            max = len(vis)

    print(max)

    return max


