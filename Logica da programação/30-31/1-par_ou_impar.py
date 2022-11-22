numero = input("Digite um número inteiro: ")

if numero.isnumeric():
    numero = int(numero)

    par_imp = numero % 2

    if par_imp == 0:
        print("Par")
    else:
        print("Ímpar")
else:
    print("Esse valor não é um número inteiro.")
