print('#' * 120)
print('Programa que conta numeros primos, verifica quantos números primos tem de zero até o número escolhido')
print('#' * 120)

quantidade_maxima = int(input('Digite um número escolhido'))

contador = 0
numero = 2
divisor = 1
vetor_primos = []
soma_primos = 0

while numero <= quantidade_maxima:
    while divisor <= numero:
        if numero % divisor == 0:
            contador += 1
        divisor += 1
    if contador == 2:
        vetor_primos.append(numero)
    numero += 1
    divisor = 1
    contador = 0

for numero in vetor_primos:
    soma_primos += numero

print(f'Os número primos até {quantidade_maxima} são: {vetor_primos}. A soma dos números primos é: {soma_primos}')
print('FIM DO PROGRAMA')

# i = 2
# j = 1

# while i <= quantidade_maxima:
#     while j <= i:
#         if i % j == 0:
#             contador += 1
#         j += 1
#     if contador == 2:
#         print(i)
#     i += 1
#     j = 1
#     contador = 0

