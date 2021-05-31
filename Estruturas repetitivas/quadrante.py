x = int(input('Digite a coordenada "X"'))
y = int(input('Digite a coordenada "Y"'))

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Coordenada Q1')
    elif x < 0 and y > 0:
        print('Coordenada Q2')
    elif x < 0 and y < 0:
        print('Coordenada Q3')
    else:
        print('Coordenada Q4')
    
    x = int(input('Digite a coordenada "X"'))
    y = int(input('Digite a coordenada "Y"'))

print('Fim do programa!')