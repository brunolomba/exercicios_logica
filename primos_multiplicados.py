def num_primorial(n):
    valor_maximo = n * n
    maximo = [0 for x in range(valor_maximo)]
    primos = []
    contador = True

    for i in range(2, valor_maximo):
        maximo[i] = i

    i = 2
    while contador:
        if maximo[i] == i:
            primos.append(i)
            for j in range(i+i, valor_maximo, i):
                maximo[j] = 0

        if len(primos) == n:
            contador = False

        i += 1

    maximo.remove(0)
    resultado = 1
    for numero in primos:
        resultado *= numero

    return resultado

print(num_primorial(4))