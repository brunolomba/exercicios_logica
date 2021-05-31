print('#' * 120)
print('Programa armazena números em um array mostra a média dele e quais números estão abaixo da média.')
print('#' * 120)

numeros = int(input('Digite quantos números que você deseja acrescentar no array.'))

array_notas = [float(input('Digite os valores da notas')) for i in range(numeros)]
# for i in range(numeros):
#     array_notas.append(float(input('Digite os valores da notas')))


# VERSÃO SIMPLIFICADA DO PYTHON
media_array = sum(array_notas) / len(array_notas)

notas_abaixo_media = [i for i in array_notas if i < media_array]
# for i in array_notas:
#     if i < media_array:
#         notas_abaixo_media.append(i)
#         print(i)

# VERSÃO DA AULA
# soma_array = 0

# for i in array_notas:
#     soma_array += i

# media_array = soma_array / numeros
 
print(f' A media do array de notas é {media_array} e os elementos abaixo da média são {notas_abaixo_media}.')
print('Fim do programa')