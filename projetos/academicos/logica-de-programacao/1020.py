IdadeDias = int(input())

Anos = IdadeDias//365
Dias = IdadeDias%365
Meses = Dias//30
Dias = Dias%30

print(f'{Anos} ano(s)')
print(f'{Meses} mes(es)')
print(f'{Dias} dia(s)')
            