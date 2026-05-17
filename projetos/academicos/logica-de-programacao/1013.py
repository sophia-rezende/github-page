A, B, C = map(float,input(). split())

def Maior(A, B):
    return int((A + B + abs(A - B)) / 2)

print(f'{Maior(Maior(A, B),C)} eh o maior')
#{Maior(Maior(A, B),C)}
# Maior(A, B) vai fazer a conta de quem é maior entre A e B
#agora o Maior antes disso faz a conta agora com a variavel C


    
