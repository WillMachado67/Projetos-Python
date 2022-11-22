"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""


def salutation(v1, v2):
    print(f'{v1} {v2}.')


salute = input('Digite a saudação: ')
name = input('Digite seu nome: ')

salutation(salute, name)
