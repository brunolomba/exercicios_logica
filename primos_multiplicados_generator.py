# def num_primorial(n):
#     valor_maximo = n * n
#     maximo = [0 for x in range(valor_maximo)]
#     primos = []
#     contador = True

#     for i in range(2, valor_maximo):
#         maximo[i] = i

#     i = 2
#     while contador:
#         if maximo[i] == i:
#             primos.append(i)
#             for j in range(i+i, valor_maximo, i):
#                 maximo[j] = 0

#         if len(primos) == n:
#             contador = False

#         i += 1

#     maximo.remove(0)
#     resultado = 1
#     for numero in primos:
#         resultado *= numero

#     return resultado

# print(num_primorial(4))

def iq_test(numbers):
    separacao = numbers.replace(' ', ',')
    divisao = separacao.split(',')
    lista = [int(x) for x in divisao]
    print(lista)
    count_par = 0
    count_impar = 0
    posicao_pares = []
    posicao_impares = []
    
    for i, numero in enumerate(lista):
        if numero % 2 == 0:
            count_par += 1
            posicao_pares.append(i)
        else:
            count_impar += 1
            posicao_impares.append(i)
    print(posicao_impares)
    print(posicao_pares)
    if count_par < 2:
        return posicao_pares[0] + 1
    elif count_impar < 2:
        return posicao_impares[0] + 1
    
print(iq_test('2 4 7 8 10'))
print(iq_test('1 2 2'))