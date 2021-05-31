print('#' * 120)
print('Escolha uma quantidade de notas, sendo a primeira (peso 2), segunda (peso 3), terceira (peso 4) as demais (peso1).')
print('#' * 120)

quantidade_notas = int(input('Digite quantos notas você deseja digitar.'))
nota_peso2 = 0
nota_peso3 = 0
nota_peso5 = 0
nota_peso1 = 0
media_ponderada = 0

for notas in range(1, quantidade_notas + 1):
    nota = float(input('Digite a nota do aluno.'))

    if notas == 1:
        nota_peso2 = nota * 2
    elif notas == 2:
        nota_peso3 = nota * 3
    elif notas == 3:
        nota_peso5 = nota * 5
    else:
        nota_peso1 += nota
else:
    media_ponderada = (nota_peso2 + nota_peso3 + nota_peso5 + nota_peso1) / (quantidade_notas + 7)
    print(f'A média ponderada é de {media_ponderada}.')

# EXEMPLO COM O PESO DAS NOTAS NO CÁLCULO

# quantidade_notas = int(input('Digite quantos notas você deseja digitar.'))
# nota1 = 0
# nota2 = 0
# nota3 = 0
# nota_extra = 0
# media_ponderada = 0

# for notas in range(1, quantidade_notas + 1):
#     nota = float(input('Digite a nota do aluno.'))

#     if notas == 1:
#         nota1 = nota
#     elif notas == 2:
#         nota2 = nota
#     elif notas == 3:
#         nota3 = nota
#     else:
#         nota_extra = nota_extra + nota
# else:
#     media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5 + nota_extra) / (quantidade_notas + 7)
#     print(f'A média ponderada é de {media_ponderada}.')

print('Fim do programa')