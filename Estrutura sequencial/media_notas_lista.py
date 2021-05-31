notas = []

nota1 = notas.append(int(input('Digite a primeira nota')))
nota2 = notas.append(int(input('Digite a segunda nota')))
nota3 = notas.append(int(input('Digite a terceira nota')))

media = sum(notas) / len(notas)

print(notas)
print(media)