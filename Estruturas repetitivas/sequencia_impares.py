print('#' * 120)
print('sequencia de números ímpares de 1 até "X"')
print('#' * 120)

x = int(input('Digite um número "X"'))

if x % 2 != 0:
    x += 1
    for numero in range(x):
        if numero % 2 != 0:
            print(numero)
else:
    for numero in range(x):
        if numero % 2 != 0:
            print(numero)

print('Fim do programa')