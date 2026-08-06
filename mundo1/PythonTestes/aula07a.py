n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2 
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s}', end = ' ')
print(f'A multiplicação vale {m}')
print(f'A divisão vale {d:.3f}')
print(f'A divisão inteira vale {di}')
print(f'A potência vale {e}')