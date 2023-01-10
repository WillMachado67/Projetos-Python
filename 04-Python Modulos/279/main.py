# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta


def calcular_juros(taxa, tempo):
    juros = (1 + taxa) ** tempo
    return juros


tempo = 60
tempo_anos = tempo / 12
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_meses = relativedelta(months=tempo)
data_final = data_emprestimo + delta_meses
juros_total = calcular_juros(0.3, tempo_anos)

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela_real = valor_total / numero_parcelas
valor_parcela_juros = valor_parcela_real * juros_total
total_a_pagar = 0

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela_juros:,.2f}')
    total_a_pagar += valor_parcela_juros

print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_meses.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela_juros:,.2f}.'
)
print(f'Total a ser pago R${total_a_pagar:,.2f}')
