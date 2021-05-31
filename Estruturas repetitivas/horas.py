duracao = int(input('Digite uma duracao'))

horas = int(duracao / 3600)
resto = duracao % 3600
minutos = int(resto / 60)
segundos = resto % 60

print(f'A duração é de {horas}: {minutos}: {segundos}')