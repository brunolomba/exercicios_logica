largura = int(input('Digite um a largura do terreno'))
comprimento = int(input('Digite o comprimento do terreno'))
valor_metro = int(input('Digite o valor do metro quadrado'))

area = largura * comprimento
preco = area * valor_metro

print(f' o valor do terreno é: {preco}')