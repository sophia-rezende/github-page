from math import sqrt
A, B, C = map(float, input(). split())
# bhaskara = -b +- raiz de delta / 2 * a
#delta = b **2 - 4 * a * c
delta = (B ** 2) - (4 * A * C)
if delta < 0 or A==0:
    print('Impossível calcular')
    
else:
    x1 = (-B + sqrt(delta)) / (2 * A)
    x2 = (-B - sqrt(delta)) / (2 * A)
    print (f'R1 = {x1:.5f}')
    print (f'R2 = {x2:.5f}')