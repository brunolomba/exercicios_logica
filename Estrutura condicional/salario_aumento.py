salario = float(input('Digite o salário'))
porcentagem = 0

if salario <= 1000:
    porcentagem = 20
elif salario <= 3000:
    porcentagem = 15
elif salario <= 8000:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario * porcentagem / 100
novo_salario = salario + aumento
diferenca = novo_salario - salario

print(f'O novo salário com a margem de {porcentagem}% a mais é de {novo_salario} com uma diferença de {diferenca} reais')