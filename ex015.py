# Exercicio 15 escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

KM = float(input('Quantos KM você andou?'))
dias = int(input('quantos dias você ficou com o carro?'))

print('O total a pagar é {}'.format(KM*0.15+dias*60))