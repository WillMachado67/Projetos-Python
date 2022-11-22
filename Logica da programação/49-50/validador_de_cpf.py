"""
CPF = 168.995.350-09
------------------------------------------
1 * 10 = 10           #   1 * 11 = 11 <-
6 * 9  = 54           #   6 * 10 = 60
8 * 8  = 64           #   8 *  9 = 72
9 * 7  = 63           #   9 *  8 = 72
9 * 6  = 54           #   9 *  7 = 63
5 * 5  = 25           #   5 *  6 = 30
3 * 4  = 12           #   3 *  5 = 15
5 * 3  = 15           #   5 *  4 = 20
0 * 2  = 0            #   0 *  3 = 0
                      # ->0 *  2 = 0
        297           #            343
11 - (297 % 11) = 11  #    11 - (343 % 11) = 9
11 > 9 = 0            #
Digíto 1 = 0          #  Digíto 2 = 9
"""

cpf = input('Digite um CPF que deseja validar: ')
if not cpf.isnumeric():
    print('Ops! Você não colocou um cpf.')
else:
    *list_cpf, d1, d2 = cpf
    cont_d1 = 10
    cont_d2 = 11
    list_d1 = []
    list_d2 = []
    new_cpf = ""

    for n1 in list_cpf:
        n1 = int(n1)
        last_list = n1 * cont_d1
        cont_d1 -= 1
        list_d1.append(last_list)
        new_cpf += str(n1)

    sum_list_d1 = sum(list_d1)

    digit_1 = 11 - (sum_list_d1 % 11)

    if digit_1 > 9:
        digit_1 = 0

    list_cpf.append(digit_1)

    for n2 in list_cpf:
        n2 = int(n2)
        last_list = n2 * cont_d2
        cont_d2 -= 1
        list_d2.append(last_list)

    sum_list_d2 = sum(list_d2)
    digit_2 = 11 - (sum_list_d2 % 11)

    new_cpf += str(digit_1)
    new_cpf += str(digit_2)

    if cpf == new_cpf:
        print('CPF Válido')
    else:
        print('CPF Inválido')
