print('#' * 120)
print('Teste de manipulação de Strings')
print('#' * 120)

nome = 'Maria'
print(nome.split())
print(list(nome))

frase = 'Maria é minha mãe'
print(frase.split())
print(list(frase))
print('-'.join(frase.split()))
print('-'.join(frase))
print(frase.islower()) # Verificação se é minúsculo
print(frase.lower()) # Transforma a String em minúsculo

print('FIM DO PROGRAMA')