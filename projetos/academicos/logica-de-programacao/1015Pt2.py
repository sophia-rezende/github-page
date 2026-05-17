from math import sqrt
#from é para chamar a biblioteca e import é para importar
#sqrt vem de square root que é o mesmo que raiz quadrada

x1, y1 = map(float, input(). split(' '))
x2, y2 = map(float, input(). split(' '))

print(f'{(sqrt((x2 - x1)**2 + (y2 - y1)**2)):.4f}')