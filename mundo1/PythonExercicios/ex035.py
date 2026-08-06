a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Os lados formam um triângulo.')
else:
    print('Os lados não formam um triângulo.')