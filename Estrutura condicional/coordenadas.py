x = int(input('Digite a coordenada "X"'))
y = int(input('Digite a coordenada "Y"'))

if x > 0 and y > 0:
    print('Coordenada Q1')
elif x < 0 and y > 0:
    print('Coordenada Q2')
elif y == 0:
    print('Eixo Y')
elif x < 0 and y < 0:
    print('Coordenada Q3')
elif x > 0 and y < 0:
    print('Coordenada Q4')
elif x == 0:
    print('Eixo x')
else:
    print('Origem')