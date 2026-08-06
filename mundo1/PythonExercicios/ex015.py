dias = int(input('Quantos dias você ficou com o carro alugado? '))
km = float(input('Quantos km você rodou com o carro? '))
valor = (dias * 60) + (km * 0.15)
print(f'O valor a ser pago é: R${valor:.2f}')