salario = float(input('Digite o salário do funcionário: '))
if salario <= 1250:
    print(f'O novo salário do funcionário é de R$ {salario * 1.15:.2f}')
else:
    print(f'O novo salário do funcionário é de R$ {salario * 1.10:.2f}')