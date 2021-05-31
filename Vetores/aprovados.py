print('#' * 120)
print('Programa armazena nome dos alunos e as notas do 1. e 2. semestre, a mostra os alunos aprovados com notas acima de 6.0.')
print('#' * 120)

numeros = int(input('Digite quantos númros que você deseja acrescentar no array.'))
array_alunos = []
array_1_semestre = []
array_2_semestre = []
soma_semestres = []
media_semestres = []
aprovados = []

for i in range(numeros):
    print(f'Digite os dados do {i + 1} Aluno')
    nome_aluno = input('Digite o nome do aluno')
    array_alunos.append(nome_aluno)

    notas_1 = float(input('Digite do 1 semestre'))
    while notas_1 < 0 or notas_1 > 10:
        notas_1 = float(input('Digite uma nota válida entre 0 e 10'))
    array_1_semestre.append(notas_1)

    notas_2 = float(input('Digite do 2 semestre'))
    while notas_2 < 0 or notas_2 > 10:
        notas_2 = float(input('Digite uma nota válida entre 0 e 10'))
    array_2_semestre.append(notas_2)

for i in range(numeros):
    media_semestres.append((array_1_semestre[i] + array_2_semestre[i]) / 2)
    if media_semestres[i] > 6:
        print(array_alunos[i])
        aprovados.append(array_alunos[i])    
        
print(f'Os Alunos que estão aprovados são {aprovados}.')
print('Fim do programa')