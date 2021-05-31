horario_inicial = int(input('Digite a hora de início do jogo'))
horario_final = int(input('Digite a hora de início do jogo'))
duracao = 0

if horario_inicial > horario_final:
    duracao = 24 - horario_inicial + horario_final
else:
    duracao = horario_final - horario_inicial

print(f'O jogo iníciou às {horario_inicial}H e terminou às {horario_final}H, com um tempo de jogo de {duracao}H.')