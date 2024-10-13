print('Crie um programa que leia quanto dnheiro uma pessoa tem em carteira e mostre quantos doláres ela pode comprar. '
      '\n Considere USS1,00= R$3,27')
real = float(input('Digite um valor em reais: R$ '))
dolar = real / 3.27
print('Real: R${:.2f}\nDolár:${:.2f}'.format(real, dolar))