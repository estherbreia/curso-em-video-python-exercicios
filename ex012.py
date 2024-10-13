print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')
p = float(input('Valor do produto: R$ '))
novo = p-(p*5/100)
print('Valor: R$ {:.2f} \nValor com desconto de 5%: R$ {:.2f}'.format(p, novo))

