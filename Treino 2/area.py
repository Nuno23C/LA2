'''
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

mapa = ["..*..",
        ".*.*.",
        "*...*",
        ".*.*.",
        "..*.."]
  
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
    return (0 <= x < len(mapa)) and (0 <= y < len(mapa)) and mapa[y][x] == "."
    

def area(p,mapa):
    adj = {}
    
    for y in range(len(mapa)):
        for x in range(len(mapa)):
            if (x,y) not in adj:
                adj[(x,y)] = []
            
            if verifica(mapa,x+1,y):
                adj[(x,y)].append((x+1,y))
                
            if verifica(mapa,x-1,y):
                adj[(x,y)].append((x-1,y))
                
            if verifica(mapa,x,y+1):
                adj[(x,y)].append((x,y+1))
                
            if verifica(mapa,x,y-1):
                adj[(x,y)].append((x,y-1))
    
    print(adj)
    
    vis = dfs(adj,p)
    
    return len(vis)
