N = int(input("Qual é a ordem da matriz? "))

mat = [[0 for x in range(N)]for x in range(N)]

for i in range(0,N):
    for j in range(0,N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

SomaPositivos = 0
for i in range(0,N):
    for j in range(0,N):
        if mat[i][j] > 0:
            SomaPositivos = SomaPositivos + mat[i][j]
print(f"A soma dos positivos é {SomaPositivos}")
print()

Linha = int(input("Escolha uma linha: "))
for j in range(0,N):
    print(f"{mat[Linha][j]} ", end="")
print()

Coluna = int(input("Escolha uma coluna: "))
for i in range(0,N):
    print(f"{mat[i][Coluna]} ", end="")
print()

print("Diagonal Principal")
for i in range(0,N):
    for j in range(0,N):
        if i == j:
            print(f"{mat[i][j]} ", end="")
print()
print("Matriz Alterada")
for i in range(0,N):
    for j in range(0,N):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] * mat[i][j]
        print(f"{mat[i][j]} ", end="")
    print()