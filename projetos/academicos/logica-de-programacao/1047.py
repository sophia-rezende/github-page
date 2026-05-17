HoraInicial, MinutoInicial, HoraFinal, MinutoFinal = map(int, input().split())  

if HoraInicial >= HoraFinal and MinutoInicial >= MinutoFinal:
    DuracaoHoras = 24 - HoraInicial + HoraFinal
    if DuracaoHoras == 24:
        DuracaoHoras = 24
        DuracaoMinutos = 0
        print(f'O JOGO DUROU {DuracaoHoras} HORA(S) E {DuracaoMinutos} MINUTO(S)')
    elif DuracaoHoras == 1 and ((60 - MinutoInicial + MinutoFinal) < 0):
        DuracaoHoras = 0
        DuracaoMinutos = (60 - MinutoInicial) + MinutoFinal
        print(f'O JOGO DUROU {DuracaoHoras} HORA(S) E {DuracaoMinutos} MINUTO(S)')
    elif DuracaoHoras > 1:
        DuracaoMinutos = 60 - MinutoInicial + MinutoFinal
        print(f'O JOGO DUROU {DuracaoHoras} HORA(S) E {DuracaoMinutos} MINUTO(S)')

else:
    DuracaoHoras = HoraFinal - HoraInicial
    DuracaoMinutos = MinutoFinal - MinutoInicial
    print(f'O JOGO DUROU {DuracaoHoras} HORA(S) E {DuracaoMinutos} MINUTO(S)')



#CONTINUAR A TENTAR EM CASA 