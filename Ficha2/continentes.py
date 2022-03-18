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
    # vizinhos = [["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]

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

    '''
    ligados = {'Luxemburgo': ['Franca', 'Belgica', 'Alemanha'],
               'Alemanha': ['Franca', 'Belgica', 'Luxemburgo'],
               'Canada': ['Estados Unidos'],
               'Franca': ['Espanha', 'Belgica', 'Alemanha', 'Luxemburgo'],
               'Espanha': ['Portugal', 'Franca'],
               'Belgica': ['Franca', 'Alemanha', 'Luxemburgo'],
               'Portugal': ['Espanha'],
               'Estados Unidos': ['Canada']}
    '''

    paises = list(ligados.keys())

    continentes = {}

    num = 0
    for o in ligados:
        vis = bfs(ligados,o)
        for pais in paises:
            if pais in vis and pais not in continentes:
                continentes[pais] = num
        num += 1

    print(continentes)

    valores = list(continentes.values())

    print(valores)

    dic = {}
    for valor in valores:
        if valor not in dic:
            dic[valor] = 1
        else:
            dic[valor] += 1

    print(dic)

    m = max(list(dic.values()))

    return m
