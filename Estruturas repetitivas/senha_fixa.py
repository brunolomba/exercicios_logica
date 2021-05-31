print('#' * 120)
print('Digite as idades para saber a media ou um número negativo para finalizar')
print('#' * 120)

senha = int(input('Digite sua senha'))

while senha != 2002:
    print('Senha inválida')
    senha = int(input('Digite corretamento seu senha'))

print('Acesso permitido!')
