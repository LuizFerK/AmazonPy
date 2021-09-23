from carts import cart
from products import product

def call(userCpf):
  purchases = []
  products = product.getAll()
  counter = 0

  with open('databases/purchases.csv','r') as file:
    for row in file:
      bdUserCpf, productId, quantity = row.replace('\n', '').split(', ')

      if bdUserCpf == userCpf:
        purchases.append(cart.build(userCpf, productId, quantity))

  if len(purchases) == 0:
    return print("\nVocê ainda não fez nenhuma compra!")


  print(f"\nSuas compras:\n")

  for i in purchases:
    counter += 1

    for p in products:
      if i.userCpf == userCpf and i.productId == p.id:
        itemValue = round(int(i.quantity) * float(p.value), 2)
        print(f"{counter} - {p.name}. Quantidade: {i.quantity}. Valor unitário: R${float(p.value):.2f}. Valor total: R${(itemValue):.2f}")