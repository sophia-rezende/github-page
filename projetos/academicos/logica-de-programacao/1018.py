Valor = int(input())

Cedulas = [100, 50, 20, 10, 5, 2, 1]

print(Valor)

for nota in Cedulas:
    Quantidade = Valor // nota
    Valor = Valor%nota

    print(f'{Quantidade} nota(s) de R$ {nota},00')