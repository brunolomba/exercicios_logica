print('#' * 120)
print('''Programa que conta conta quantas cédulas precisa dar para o cliente no caixa eletrônico.
        Serão usadas cédulas de 100, 50, 20, 10, 5, 2, 1.''')
print('#' * 120)

valor = int(input('Digite quanto você deseja sacar.'))
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
notas_1 = 0
resto = 0

# Resolução com while e IFs

while True:
    if valor >= 100:
        valor = valor - 100
        notas_100 += 1
    elif valor >= 50:
        valor = valor - 50
        notas_50 += 1
    elif valor >= 20:
        valor = valor - 20
        notas_20 += 1
    elif valor >= 10:
        valor = valor - 10
        notas_10 += 1
    elif valor >= 5:
        valor = valor - 5
        notas_5 += 1
    elif valor >= 2:
        valor = valor - 2
        notas_2 += 1
    elif valor >= 1:
        valor = valor - 1
        notas_1 += 1
    else:
        break 

print(f'Notas de 100 : {notas_100}')
print(f'Notas de 50 : {notas_50}')
print(f'Notas de 20 : {notas_20}')
print(f'Notas de 10 : {notas_10}')
print(f'Notas de 5 : {notas_5}')
print(f'Notas de 2 : {notas_2}')
print(f'Notas de 1 : {notas_1}')
print(resto)
print('FIM DO PROGRAMA')