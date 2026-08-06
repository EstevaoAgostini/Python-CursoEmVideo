preco = int(input('Digite o preço do produto: R$'))
desconto = preco * 0.05
valorf = preco - desconto

print(f'Valor com desconto e 5%: R${valorf:.2f}')