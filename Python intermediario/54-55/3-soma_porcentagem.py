"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def percent_sum(n, p):
    calculate_percent = (p / 100)
    discover_percent = n * calculate_percent
    return n + discover_percent


number = int(input('Digite um numero: '))
percent = int(input('Digite a porcentagem: '))

sum = percent_sum(number, percent)

print(f'A soma de {number} com {percent}% é {sum}')
