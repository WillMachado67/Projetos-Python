
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

print(carrinho)

total = sum([produto[1] for produto in carrinho])

print(total)

# total = 0
# for produto in carrinho:
#     total += produto[1]
# print(total)

# total = []
# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))
