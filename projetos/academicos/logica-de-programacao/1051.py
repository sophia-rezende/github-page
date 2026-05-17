Salario = float(input())

if Salario > 2000:
    if Salario <= 3000:
        imposto = (Salario - 2000) * 0.08
        print(f'R$ {imposto:.2f}')
    elif Salario <= 4500:
        DIF1 = Salario - 3000
        imposto = (Salario - 2000 - DIF1) * 0.08 + (DIF1 * 0.18)
        print(f'R$ {imposto:2f}')
    elif Salario > 4500:
        DIF1 = Salario - 4500
        DIF2 = Salario - 3000
        DIF3 = Salario - 2000
        imposto = (DIF1 * 0.28) + ((DIF2 - DIF1) * 0.18) + ((DIF3 - DIF2 - DIF3) * 0.08)
        print(f'R$ {imposto:.2f}')
else:
    print('Isento')