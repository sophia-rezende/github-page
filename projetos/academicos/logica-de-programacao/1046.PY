Inicial, Final = map(int, input().split())

if Inicial >= Final:
    print(f'O JOGO DUROU {24 - Inicial + Final} HORA(S)')
else:
    print(f'O JOGO DUROU {Final - Inicial} HORA(S)')
