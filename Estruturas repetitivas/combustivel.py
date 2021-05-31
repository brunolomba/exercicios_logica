codigo = int(input('Digite o código 1-alcool, 2-gasolina, 3-diesel ou 4 para parar'))
alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    else:
        codigo = int(input('digite um código válido ou 4 para encerrar.'))
    codigo = int(input('Digite o código 1-alcool, 2-gasolina, 3-diesel ou 4 para parar'))

print(f'Muito Obrigado! Foram abastecidos {alcool} com alcool, {gasolina} com gasolina, {diesel} com disel.')