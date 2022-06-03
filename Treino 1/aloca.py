'''
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto,
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
'''

def aloca(prefs):
    new_prefs = list(prefs.items())
    new_prefs.sort(key = lambda x : (x[0]))
    
    projects = {}
    alunoNaoAlocs = []

    for aluno in new_prefs:
        projects_alocated = projects.values()
        for project in aluno[1]:
            if project not in projects_alocated and aluno[0] not in projects:
                projects[aluno[0]] = project
        if aluno[0] not in projects:
            alunoNaoAlocs.append(aluno[0])

    return alunoNaoAlocs
