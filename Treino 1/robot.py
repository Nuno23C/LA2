'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita
  'H' - parar e regressar à posição inicial virado para cima

Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    movimentos = {
        0 : (0,1),    # Cima
        1 : (1,0),    # Direita
        2 : (0,-1),   # Baixo
        3 : (-1,0)    # Esquerda
    }
    viradoPara = 0
    pos = [0,0]   # (x,y)
    max_X = 0
    min_X = 0
    max_Y = 0
    min_Y = 0
    r = []

    for comando in comandos :
        if comando == 'A' :
            pos[0] += movimentos[viradoPara][0]
            pos[1] += movimentos[viradoPara][1]
            if(pos[0] > max_X) :
                max_X = pos[0]
            elif(pos[0] < min_X) :
                min_X = pos[0]
            if (pos[1] > max_Y) :
                max_Y = pos[1]
            elif(pos[1] < min_Y) :
                min_Y = pos[1]
        elif comando == 'E' :
            viradoPara = (viradoPara - 1) % 4
        elif comando == 'D' :
            viradoPara = (viradoPara + 1) % 4
        else :
            r.append((min_X,min_Y,max_X,max_Y))
            max_X = 0
            max_Y = 0
            min_X = 0
            min_Y = 0
            pos[0] = 0
            pos[1] = 0
            viradoPara = 0

    return r


def main():
    print("<h3>robot</h3>")
    cs = "EEAADAAAAAADAAAADDDAAAHAAAH"
    print("in:",cs)
    print("out:",robot(cs))
