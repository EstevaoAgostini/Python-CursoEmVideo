from math import hypot

c_oposto = int(input('Digite o valor do cateto oposto: '))
c_adjacente = int(input('Digite o valor do cateto adjacente: '))

print(f'A hipotenusa vale {hypot(c_oposto, c_adjacente)}')