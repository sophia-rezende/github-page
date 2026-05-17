DiaA = int(input().split()[1])
HoraA, MinutoA, SegundoA = map(int, input().split(' : '))
DiaB = int(input().split()[1])
HoraB, MinutoB, SegundoB = map(int, input().split(' : '))

segundos = (SegundoB - SegundoA) % 60
SegundoMaior = SegundoA > SegundoB

minutos = (MinutoB - MinutoA - int(SegundoMaior)) % 60
#int(SegundoMaior) - estrutura da mat booleana - usado aqui para restringir
MinutoMaior = MinutoA > MinutoB

horas = (HoraB - HoraA - int(SegundoMaior) or int(MinutoMaior)) % 24
HoraMaior = HoraA > HoraB

Dias = DiaB - DiaA - (int(SegundoMaior) or int(MinutoMaior) or int(HoraMaior))

print(f'{Dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')