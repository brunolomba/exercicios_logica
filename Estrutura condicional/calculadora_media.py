print('Bem vindo ao programa de cálculo de média escolar!')

nome = input('Digite o seu nome?')
materia = input('Digite qual é a matéria?')

n1 = float(input('Digite sua nota n1?'))
n2 = float(input('Digite sua nota n2?'))
n3 = float(input('Digite sua nota n3?'))
n4 = float(input('Digite sua nota n4?'))

media = (n1 + n2 + n3 + n4) / 4

if media < 7:
    print(f'O {nome} foi Reprovado em {materia} e sua nota foi {media}.')
else:
     print('O %s, foi Aprovado em %s e sua nota foi %.2f.' % (nome, materia, media))