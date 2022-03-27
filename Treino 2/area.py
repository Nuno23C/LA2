'''
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.

         01234
mapa = ["..*..", 0
        ".*.*.", 1         x y
        "*..o*", 2    o = (3,2)
        ".*.*.", 3
        "..*.."] 4

'''

def dfs(adj,o):
    return dfs_aux(adj,o,set())

def dfs_aux(adj,o,vis):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            dfs_aux(adj,d,vis)
    return vis


def verifica(mapa,x,y):
    return (0 <= x < len(mapa)) and (0 <= y < len(mapa)) and mapa[x][y] != "*"


def area(p,mapa):
    adj = {}

    if(len(mapa) == 0):
        return 0

    if(mapa[p[0]][p[1]] == "*"):
        return 0

    for i in range(len(mapa)):
        for j in range(len(mapa)):
            adj[(j,i)] = []
            # Esquerda
            if verifica(mapa,j-1,i):
                adj[(j,i)].append((j-1,i))
            # Direita
            if verifica(mapa,j+1,i):
                adj[(j,i)].append((j+1,i))
            # Cima
            if verifica(mapa,j,i-1):
                adj[(j,i)].append((j,i-1))
            # Baixo
            if verifica(mapa,j,i+1):
                adj[(j,i)].append((j,i+1))

    print(adj)

    p = (p[1],p[0])
    vis = dfs(adj,p)

    print(vis)

    return len(vis)
