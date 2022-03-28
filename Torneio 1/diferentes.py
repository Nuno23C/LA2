'''
Defina uma função que, dada uma lista de strings, retorne
essa lista ordenada por ordem decrescente do número de
caracteres diferentes nela contidos.
Caso duas strings tenham o mesmo número de caracteres
diferentes a mais pequena em ordem lexicográfica deve
aparecer primeiro na lista retornada.
'''

def diferentes(frases):
    r = []

    for frase in frases:
        difs = len(list(set(frase)))
        r.append((frase,difs))

    r.sort(key= lambda x: (-x[1],x[0]))

    r2 = [ x[0] for x in r]

    return r2
