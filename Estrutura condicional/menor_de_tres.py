a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))
menor = 0

if a < b and a < c:
    menor = a
else:
    if b < c:
        menor = b
    else:
        menor = c

# if a < b and a < c:
#     menor = a
# elif b < c:
#     menor = b
# else:
#     menor = c

print(f'O menor valor entre os três números é o {menor}')