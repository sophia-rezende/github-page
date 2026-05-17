Valor = float(input())

if 100 < Valor:
    print('Fora de intervalo')
elif 75 < Valor :
    print('Intervalo (75,100]')
elif 50 < Valor :
    print('Intervalo (50,75]')
elif 25 < Valor :
    print('Intervalo (25,50]')
elif 0 <= Valor:
    print('Intervalo (0,25]')
else:
    print('Fora de intervalo')