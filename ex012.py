# Exercicio 12 faça um algoritimo que leia o peço de um produto e mostre o seu novo preço, com 5% de desconto

preço = float(input('qual o preço do produto?'))

print('o produto que custava R${}, na promoção com 5% de desconto vai custar {:.2f}'.format(preço, preço / 100 * 5))
