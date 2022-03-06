'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras,
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas
por ordem alfabética.
'''

def frequencia(texto):
    # texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    lista = {}
    texto = texto.split(' ')

    for palavra in texto:
        if palavra not in lista:
            lista[palavra] = 1
        else:
            lista[palavra] += 1

    # lista = {'perguntou': 1, 'ao': 1, 'tem': 1, 'quanto': 1, 'tempo': 4, 'o': 2}

    novaLista = list(lista.items())
    novaLista.sort(key = lambda x : (-x[1],x[0]))
    # novaLista = [('tempo', 4), ('o', 2), ('ao', 1), ('perguntou', 1), ('quanto', 1), ('tem', 1)]
    listaFinal = [x[0] for x in novaLista]

    return listaFinal
