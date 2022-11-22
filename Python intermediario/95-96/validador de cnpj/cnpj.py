import re
from itertools import count


def validate(cnpj):
    cleanCnpj = clean_cnpj(cnpj)
    digit = digit_cnpf(cleanCnpj)
    digit1 = first_digit(digit)
    digit.append(str(digit1))
    digit2 = second_digit(digit)
    digit.append(str(digit2))
    new_cnpj = digit
    return new_cnpj


def clean_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def digit_cnpf(cnpj):
    *cnpj, d1, d2 = cnpj
    return cnpj


def first_digit(cnpj):
    count = 5
    calc_cnpj = []
    for d in cnpj:
        calc = int(d) * count
        calc_cnpj.append(calc)
        count -= 1
        if count < 2:
            count = 9
    sum_digit = sum(calc_cnpj)
    digit1 = 11 - (sum_digit % 11)
    if digit1 > 9:
        digit1 = 0
    return digit1


def second_digit(cnpj):
    count = 6
    calc_cnpj = []
    for d in cnpj:
        calc = int(d) * count
        calc_cnpj.append(calc)
        count -= 1
        if count < 2:
            count = 9
    sum_digit = sum(calc_cnpj)
    digit2 = 11 - (sum_digit % 11)
    if digit2 > 9:
        digit2 = 0
    return digit2
