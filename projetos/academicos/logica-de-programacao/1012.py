A, B, C = map(float,input(). split())
AreaTriangulo = (A * C) / 2
n = 3.14159
AreaCirculo= n * (C **2)
AreaTrapezio = ((A + B) * C) / 2
AreaQuadrado = B ** 2
AreaRetangulo = A * B

print(f'Triamgulo: {AreaTriangulo:.3f}')
print(f'Circulo: {AreaCirculo:.3f}')
print(f'Trapezio: {AreaTrapezio:.3f}')
print(f'Quadrado: {AreaQuadrado:.3f}')
print(f'Retangulo: {AreaRetangulo:.3f}')