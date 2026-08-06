kmh = int(input('Qual a velocidade do seu carro em km/h? '))
if kmh > 80:
    print(f'Você foi multado! O valor da multa é de R$ {(kmh - 80) * 7:.2f}')
else:
    print('Você está dentro do limite de velocidade. Tenha um bom dia!')