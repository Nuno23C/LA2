'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos.
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos,
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    # livros = {"Todos os nomes":"9789720047572", "Ensaio sobre a cegueira":"9789896604011", "Memorial do convent":"9789720046711", "Os cus de Judas":"9789722036757"}
    livrosInvalidos = {}

    for livro in livros :
        r = 0
        pos = 0
        chave = livros[livro]

        while (pos < len(chave)) :
            if (pos%2 != 0) :
                r += int(chave[pos])*3
            else :
                r += int(chave[pos])
            pos += 1

        if (r%10 != 0) :
            livrosInvalidos[livro] = livros[livro]

    return sorted(livrosInvalidos)

