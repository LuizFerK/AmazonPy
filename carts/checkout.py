from products import product
from products import purchase as productPurchase
from carts import cart
from purchases import purchase

def call(userCpf):
  def options(userCpf, cartList, finalValue):
    opt = input("\nEscolha uma opção:\n1 - Continuar comprando\n2 - Finalizar compra\n3 - Voltar ao menu\n")

    if opt == '1':
      return productPurchase.call(userCpf)
    if opt == '2':
      return purchase.checkout(userCpf, cartList, finalValue)
    elif opt == '3':
      return
    else:
      print("\nPor favor, digite uma opção válida!")
      return options(userCpf, cartList, finalValue)

  items = cart.getAllByUserCpf(userCpf)

  if len(items) == 0:
    return print("\nSeu carrinho está vazio!")

  products = product.getAll()
  cartList = []
  counter = 0
  finalValue = 0.0

  print(f"\nCarrinho ({len(items)} itens):\n")

  for i in items:
    counter += 1

    for p in products:
      if i.userCpf == userCpf and i.productId == p.id:
        itemValue = round(int(i.quantity) * float(p.value), 2)
        finalValue += itemValue
        print(f"{counter} - {p.name}. Quantidade: {i.quantity}. Valor unitário: R${float(p.value):.2f}. Valor: R${(itemValue):.2f}")
        cartList.append(cart.build(i.userCpf, i.productId, i.quantity))

  print(f"\nValor total: R${round(finalValue, 2):.2f}")

  return options(userCpf, cartList, finalValue)

