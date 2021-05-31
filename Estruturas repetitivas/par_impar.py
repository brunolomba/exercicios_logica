print('#' * 120)
print('Escolha uma quantidade de números e depois saiba se é par ou ímpar e se é positivo ou negativo.')
print('#' * 120)

n = int(input('Digite quantos números você deseja digitar.'))

for numero in range(1, n + 1):
    x = int(input('Digite um número que você desejar.'))
    if x % 2 == 0:
        if x > 0:
            print(f'O número {x} é PAR e POSITIVO.')
        elif x < 0:
            print(f'O número {x} é PAR e NEGATIVO.')
        else:
            print(f'O número {x} é NULO.')
    else:
        if x > 0:
             print(f'O número {x} é ÍMPAR e POSITIVO.')
        else:
             print(f'O número {x} é ÍMPAR e NEGATIVO.')
print('Fim do programa')

# EXEMPLO ISOLANDO O ZERO

# for numero in range(1, n + 1):
#     x = int(input('Digite um número que você desejar.'))
#    
#     if x = 0:
#         print(f'O número {x} é NULO.')
#     if x % 2 == 0:
#         if x > 0:
#             print(f'O número {x} é PAR e POSITIVO.')
#         else:
#             print(f'O número {x} é PAR e NEGATIVO.')
#     else:
#         if x > 0:
#              print(f'O número {x} é ÍMPAR e POSITIVO.')
#         else:
#              print(f'O número {x} é ÍMPAR e NEGATIVO.')