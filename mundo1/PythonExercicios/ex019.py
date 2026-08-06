from random import choice

alunos = []
for i in range(4): 
    nomes = str(input('Digite o nome do aluno: '))
    alunos.append(nomes)

aleatorio = choice(alunos)
print(f'Vez do {aleatorio} apagar o quadro!')