import random
import os

os.system('cls')

letrasmin = 'abcdefghijklmnopqrstuvwxyz'
letrasmai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '{}[].,;#_-?!=<>@$&'

possiveis = letrasmin + letrasmai + numeros + simbolos
numcaracteres = int(input('Deseja gerar uma senha de quantos caracteres?\n-> '))
senha = ''.join(random.sample(possiveis, numcaracteres))

print('='*30)
print(f'Senha gerada:\n{senha}\n')