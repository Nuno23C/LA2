'''
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

mapa = ["  ########",
        "# # #    #",
        "# # #### #",
        "# #      #",
        "# # # ####",
        "# # #    #",
        "#   # #  #",
        "##### ####",
        "#        #",
        "########  "]

'''

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai


def verifica(mapa, x, y):
    return (0 <= x < len(mapa)) and (0 <= y < len(mapa)) and mapa[x][y] != "#"


def caminhoMaisCurto(adj, o, d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)

    return caminho

def converte(caminho):
    r = ""

    for i in range(len(caminho)-1):
        par = (caminho[i+1][0] - caminho[i][0], caminho[i+1][1] - caminho[i][1])
        if(par[0] == 0 and par[1] == 1):
            r += "E"
        elif(par[0] == 0 and par[1] == -1):
            r += "O"
        elif(par[0] == 1 and par[1] == 0):
            r += "S"
        else:
            r += "N"

    return r


def caminho(mapa):
    adj= {}
    d = (len(mapa)-1,len(mapa)-1)

    for i in range(len(mapa)):
        for j in range(len(mapa)):
            adj[(j,i)] = []
            # Sul
            if verifica(mapa, j, i+1):
                adj[(j,i)].append((j, i+1))
            # Norte
            if verifica(mapa, j, i-1):
                adj[(j,i)].append((j, i-1))
            # Este
            if verifica(mapa, j+1, i):
                adj[(j,i)].append((j+1, i))
            # Oeste
            if verifica(mapa, j-1, i):
                adj[(j,i)].append((j-1, i))

    print(adj)

    c1 = caminhoMaisCurto(adj,(0,0),d)
    c2 = converte(c1)

    return c2
