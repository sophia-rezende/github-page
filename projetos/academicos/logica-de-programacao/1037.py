import math
Valor = float(input())



if Valor >= 0 and Valor <= 25:
    intervalo = [0,25]
elif Valor > 25 and <= 70:
    intervalo = [25,50]
elif Valor in [50,75]:
    intervalo = [50,75]
elif Valor in [75,100]:
    intervalo = [75,100]
    print(f'Intervalo {intervalo}')
else:
    print('Fora de intervalo') 


    
