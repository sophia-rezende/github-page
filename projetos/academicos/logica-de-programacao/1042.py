n1, n2, n3 = map(int, input().split())

if (n1 > n2 and n1 > n3) and (n2 > n3):
    print(f'{n3}')
    print(f'{n2}')
    print(f'{n1}')
elif (n1 > n2 and n1 > n3) and (n3 > n2):
    print(f'{n2}')
    print(f'{n3}')
    print(f'{n1}')
elif (n2 > n1 and n2 > n3) and (n1 > n3):
    print(f'{n3}')
    print(f'{n1}')
    print(f'{n2}')
elif (n2 > n1 and n2 > n3) and (n3 > n1):
    print(f'{n1}')
    print(f'{n3}')
    print(f'{n2}')
elif (n3 > n1 and n3 > n2) and (n1 > n3):
    print(f'{n2}')
    print(f'{n1}')
    print(f'{n3}')
elif (n3 > n1 and n3 > n2) and (n2 > n1):
    print(f'{n1}')
    print(f'{n2}')
    print(f'{n3}')


print(' ')
print(f'{n1}')
print(f'{n2}')
print(f'{n3}')
