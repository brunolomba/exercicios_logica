print('#' * 120)
print('Programa que pergunta quantos produtos deseja adicionar para saber a porcentagem de lucro, e mostra os dados.')
print('#' * 120)

numeros = int(input('Digite a quantidade de produtos que deseja verificar os lucros.'))
produtos = []
preco_compra = []
preco_venda = []
lucros = []
lucros_porcentagem = []
lucros_ate_10 = []
lucros_entre_10_20 = []
lucros_acima_de_20 = []

for i in range(numeros):
    print(f'Digite os dados do {i + 1} produto.')
    produtos.append(input('Digite o nome do primeiro produto'))
    preco_compra.append(float(input('Digite o preço de compra')))
    preco_venda.append(float(input('Digite o preço de venda do produto')))

for i in range(numeros):
    lucros.append(preco_venda[i] - preco_compra[i])
    lucros_porcentagem = lucros[i] / preco_compra[i] * 100
    
    if lucros_porcentagem < 10:
        lucros_ate_10.append(lucros_porcentagem)
        print(f'O produto {produtos[i]} está abaixo de 10%')
    elif lucros_porcentagem < 20:
        lucros_entre_10_20.append(lucros_porcentagem)
        print(f'O produto {produtos[i]} está entre 10% e 20%')
    else:
        lucros_acima_de_20.append(lucros_porcentagem)
        print(f'O produto {produtos[i]} está acima de 20%')
    
lucro_total = sum(preco_venda) - sum(preco_venda)

print(f'Os lucros abaixo de 10% são {len(lucros_ate_10)}:{lucros_ate_10}, entre 10% e 20% são {len(lucros_entre_10_20)}:{lucros_entre_10_20} e os acima de 20% são {len(lucros_acima_de_20)}:{lucros_acima_de_20}.')

print('Fim do programa')