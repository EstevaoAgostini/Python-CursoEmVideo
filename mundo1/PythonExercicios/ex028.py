import random
num = random.randint(1, 5)
escolha = int(input('Escolha um número entre 1 e 5: '))
if escolha == num:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! O número correto era {num}')