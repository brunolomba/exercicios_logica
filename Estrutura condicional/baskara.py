a = int(input('Digite o coeficiente A'))
b = int(input('Digite o coeficiente B'))
c = int(input('Digite o coeficiente C'))
delta = b ** 2 - 4 * a * c
x1 = 0
x2 = 0

if a == 0 or delta < 0:
    print('Está equação não possui raízes reais')
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f'X1 = {x1}')
    print(f'X2 = {x2}')
