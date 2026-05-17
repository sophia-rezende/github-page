N = int(input())

Horas = N//3600
M = N%3600
Minutos = N//60
N = N%60

print(f'{Horas}:{Minutos}:{N}')
               
