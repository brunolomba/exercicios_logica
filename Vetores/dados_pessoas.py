print('#' * 120)
print('Programa armazena altura e gênero das pessoas, e mostra a media das alturas de cada gênero.')
print('#' * 120)

numeros = int(input('Digite quantos pessoas você deseja passar a altura e Gênero.'))
alturas = []
generos = []
altura_mulheres = []
altura_homens = []
contador_feminino = 0
contador_masculino = 0

for i in range(numeros):
    alturas.append(float(input('Digite a altura da pessoa')))

    while True:
         genero = input('Digite o gênero da pessoa')
         if genero == 'f' or genero == 'm':
            generos.append(genero)
            break

for i in range(numeros):
    if generos[i] == 'f':
        altura_mulheres.append(alturas[i])
    else:
        altura_homens.append(alturas[i])

if len(altura_mulheres) == 0:
    print('Impossível calcular a média das alturas das mulheres')
else:
    media_mulheres = sum(altura_mulheres) / len(altura_mulheres)

if len(altura_homens) == 0:
    print('Impossível calcular a média das alturas das homens')
else:
    media_homens = sum(altura_homens) / len(altura_homens)


print(f'A maior altura do grupo é {max(alturas)} e a menor é {min(alturas)}, a média das alturas da mulheres é de {media_mulheres} e dos homens é {media_homens}, quantidade de mulheres na amostra é de {len(altura_mulheres)} e de homens é de {len(altura_homens)}.')
print('Fim do programa')