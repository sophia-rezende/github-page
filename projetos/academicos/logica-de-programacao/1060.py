NUmeros = [float(input()) for i in range(6)]

positivos = len([i for i in NUmeros if i > 0])
#ler sobre as diversas sintaxes de range e len em python.org

print(f'{positivos} valores positivos')