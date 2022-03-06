'''
Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito.

A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas.
Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.
'''

def overlap(aluno, alunos, ucs) :

    for uc1 in alunos[aluno] :
        for uc2 in alunos[aluno] :
            if (uc1 not in ucs or uc2 not in ucs) :
                return True

            else :
                startHour_uc1 = ucs[uc1][1]
                endHour_uc1 = startHour_uc1 + ucs[uc1][2]
                startHour_uc2 = ucs[uc2][1]
                endHour_uc2 = startHour_uc2 + ucs[uc2][2]

                # Se forem uc's diferentes, no mesmo dia, em horas diferentes
                if ((uc1 != uc2) and (ucs[uc1][0] == ucs[uc2][0]) and ((startHour_uc1 <= startHour_uc2 <= endHour_uc1) or (startHour_uc2 <= startHour_uc1 <= endHour_uc2))) :
                    return True

    return False

def horario(ucs, alunos) :
    alunosOK = []

    for aluno in alunos :
        if (overlap(aluno, alunos, ucs) == False) :
            alunosOK.append(aluno)

    h = 0
    r = []
    for aluno in alunosOK :
        for uc in alunos[aluno] :
            h += ucs[uc][2]
        r.append((aluno, h))
        h = 0

    r.sort(key = lambda x : (-x[1],x[0]))

    return r


def main():
    print("<h4>horario</h4>")
    ucs = {"la2": ("quarta",16,2), "pi": ("terca",15,1), "cp": ("terca",14,2),"so": ("quinta",9,3)}
    alunos = {5000: {"la2","cp"}, 2000: {"la2","cp","pi"},3000: {"cp","poo"}, 1000: {"la2","cp","so"}}
    print(horario(ucs,alunos))

if __name__ == '__main__':
    main()
