'''
O objectivo deste problema é determinar quantos movimentos são necessários para
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
'''

def bfs(o,destino):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in moves(v):
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
            if destino == d:
                return pai
    return pai


def moves(pos):
    x = pos[0]
    y = pos[1]
    return [(x+2,y+1),(x+1,y+2),(x+2,y-1),(x+1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x-1,y-2)]


def saltos(o,d):
    pai = bfs(o,d)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)

    return(len(caminho)-1)
