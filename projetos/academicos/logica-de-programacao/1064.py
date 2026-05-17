positivos = []

for i in range(6):
    numero = float(input())

    if numero > 0:
        positivos.append(numero)
        #append - armazena para usar naquele ponto

print(f'{len(positivos)} valores positivos\n{(sum(positivos) / len(positivos)):.1f}')