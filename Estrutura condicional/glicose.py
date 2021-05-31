glicose = float(input('Digite o valor da sua glicose em mg/dl'))

if glicose < 100:
    print('Normal')
elif glicose < 140:
    print('Elevado')
else:
    print('Diabetes')