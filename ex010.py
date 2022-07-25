# Exercicio 10 crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

real = float(input('quanto de dinheiro você tem?'))
dolar = real / 3.27
print('voce pode comprar US${:.2f}'.format(dolar))
