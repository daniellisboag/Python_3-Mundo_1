# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

valor = int(input('Digite um número: '))
print('O antecessor de {} é {}'.format(valor, valor - 1))
print('O sucessor de {} é {}'.format(valor, valor + 1))