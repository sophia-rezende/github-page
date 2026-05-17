Codigo, Quantidade = map(float,input().split())

if Codigo == 1:
    preco = 4.00 * Quantidade
elif Codigo == 2:
    preco = 4.50 * Quantidade
elif Codigo == 3:
    preco = 5.00 * Quantidade
elif Codigo == 4:
    preco = 2.00 * Quantidade
elif Codigo == 5:
    preco = 1.50 * Quantidade

print(f'Total: R$ {preco:.2f}')



