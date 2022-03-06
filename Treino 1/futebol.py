'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):
    tabela = {} # {equipa: [pontos,golos]}

    for jogo in jogos :
        if jogo[0] not in tabela : tabela[jogo[0]] = [0,0]
        if jogo[2] not in tabela : tabela[jogo[2]] = [0,0]

        difGolos = jogo[1] - jogo[3]

        if (jogo[1] > jogo[3]) :
            tabela[jogo[0]][0] += 3
            tabela[jogo[0]][1] += difGolos
            tabela[jogo[2]][1] -= difGolos
        elif (jogo[1] < jogo[3]) :
            tabela[jogo[2]][0] += 3
            tabela[jogo[2]][1] += difGolos
            tabela[jogo[0]][1] -= difGolos
        else :
            tabela[jogo[0]][0] += 1
            tabela[jogo[2]][0] += 1

    "r = (equipa, pontos, difGolos)"
    r = [(equipa, tabela[equipa][0], tabela[equipa][1]) for equipa in tabela]
    r.sort(key = lambda x : (-tabela[x[0]][0], -tabela[x[0]][1], x) )
    result = [(equipa[0], equipa[1]) for equipa in r]

    return result


def main():
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

if __name__ == '__main__':
    main()
