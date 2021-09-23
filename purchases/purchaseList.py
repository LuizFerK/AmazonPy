from carts import cart
from products import product

def call(userCpf):
  # Recebe todos os produtos salvos
  products = product.getAll()
  purchases = []
  counter = 0

  # Retorna todos os dados de compras do usuário
  with open('databases/purchases.csv','r') as file:
    for row in file:
      bdUserCpf, productId, quantity = row.replace('\n', '').split(', ')

      if bdUserCpf == userCpf:
        purchases.append(cart.build(userCpf, productId, quantity))

  # Retorna caso o usuário não tenha nenhuma compra
  if len(purchases) == 0:
    return print("\nVocê ainda não fez nenhuma compra!")

  # Lista todas as compras do usuário
  print(f"\nSuas compras:\n")

  for i in purchases:
    counter += 1

    for p in products:
      if i.userCpf == userCpf and i.productId == p.id:
        itemValue = round(int(i.quantity) * float(p.value), 2)
        print(f"{counter} - {p.name}. Quantidade: {i.quantity}. Valor unitário: R${float(p.value):.2f}. Valor total: R${(itemValue):.2f}")