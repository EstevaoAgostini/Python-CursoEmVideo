from math import sin, cos, tan, radians

angulo = int(input('Digite o valor do ângulo: '))
rad = radians(angulo)

print(f'Valor do seno: {sin(rad):.2f}')
print(f'Valor do cosseno: {cos(rad):.2f}')
print(f'Valor da tangente: {tan(rad):.2f}')