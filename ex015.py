print('escreva um programa que pergunte a quantidade de KM percoridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. '
      'Calcule o preço a pagar , sabendo que o carro custa R$ 60,00 por dia e R$0,15 por km rodado')
dia = int(input('Quantidade de dias: '))
km = float(input('Quilometragem: KM '))
a = (dia * 60.00) + (km * 0.15)
print('A viagem de {} dias e {} km. Custou o total de R$ {:.2f}'.format(dia, km, a))