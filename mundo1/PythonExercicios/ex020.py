from random import shuffle

alunos = []
for i in range(4): 
    nomes = str(input('Digite o nome do aluno: '))
    alunos.append(nomes)

shuffle(alunos)
print(f'A ordem de apresentação é {alunos}')