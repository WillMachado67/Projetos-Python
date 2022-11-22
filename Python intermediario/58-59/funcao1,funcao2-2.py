"""
2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor da
funcao2 executada. Faça a funcao1 executar duas funcoes que receba, um numero diferente de argumentos
"""


def func1(sdt):
    return sdt


def func2(nm):
    return nm


def func_master():
    return f'{func1(salutation)} {func2(name)}'


salutation = 'Hello'
name = 'World'


print(func_master())
