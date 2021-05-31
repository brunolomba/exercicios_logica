print('#' * 120)
print('Digite 2 números para saber se está em ordem crescente ou decrescente ou 2 números iguais para finalizar')
print('#' * 120)

x = int(input('Digite um número'))
y = int(input('Digite outro número'))

while x != y:
    if x < y:
        print('Crescente')
    else:
        print('Decrescente')

    x = int(input('Digite um número'))
    y = int(input('Digite outro número'))
       
print('Programa foi finalizado!')