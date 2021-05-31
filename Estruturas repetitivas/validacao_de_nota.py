while True:
        nota1 = int(input('Digite a primeira nota'))
        if nota1 >= 0 and nota1 <= 10:
                break

while True:
        nota2 = int(input('Digite a primeira nota'))
        if nota2 >= 0 and nota2 <= 10:
                break
     
media = (nota1 + nota2) / 2

print(f' A media das provas é de {media}.')