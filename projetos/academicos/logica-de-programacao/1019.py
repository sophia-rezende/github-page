Duracao = int(input())

horas = (Duracao//60) // 60
minutos = Duracao // 60
segundo = (Duracao/60 - Duracao//60) * 60

print(f'{horas}:{minutos}:{segundo:.0f}')