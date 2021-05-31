print('#' * 120)
print('Programa que pergunta cria uma matriz e soma as linhas.')
print('#' * 120)

while True:
    numero_linhas = int(input('Digite a quantidade de linhas.'))
    numero_colunas = int(input('Digite a quantidade de colunas.'))
    if numero_linhas <= 10 and numero_linhas > 0 and numero_colunas <= 10 and numero_colunas > 0:
        matriz = [[0 for x in range(numero_colunas)] for x in range(numero_linhas)]
        vetor_soma = [0 for x in range(numero_linhas)]
        break

# vetor_soma = []
soma = 0
posicao = 0

# Definindo o valor de cada elemento
for i in range(numero_linhas):
    print(f'Digite os elementos da linha {i + 1}:')
    for j in range(numero_colunas):
        matriz[i][j] = int(input('Digite um elemento'))

# Soma das listas
for i in range(numero_linhas):
    vetor_soma[i] = 0
    for j in range(numero_colunas):
        vetor_soma[i] += matriz[i][j]

# Soma das listas em python
# for lista in matriz:
#     soma = sum(lista)
#     vetor_soma.append(soma)
# else:
#     print(vetor_soma)

# EXEMPLO DE COMO EXIBIR A LISTA (INTERNET)
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

# print_comprehension = [print(elemento, end=' ') for lista in matriz for elemento in lista]

# Print com o posicionamento
for soma_lista in vetor_soma:
    posicao += 1
    print(f'O valor da soma da {posicao} é: {soma_lista}.')

print('Fim do programa')