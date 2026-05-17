P1 = str(input())
P2 = str(input())
P3 = str(input())

if P1 == 'vertebrado':
    if P2 == 'ave':
        if P3 == 'carnivoro':
            animal = 'aguia'
        else:
            animal = 'pomba'
    elif P2 == 'mamifero':
        if P3 == 'onivoro':
            animal = 'homem'
        else:
            animal = 'vaca'
elif P1 == 'invertebrado':
    if P2 == 'inseto':
        if P3 == 'hematofago':
            animal = 'pulga'
        else:
            animal = 'lagarta'
    elif P2 == 'anelidio':
        if P3 == 'hematofago':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'

print(f'{animal}')