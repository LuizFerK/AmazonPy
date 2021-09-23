from products import product
from products import purchase as productPurchase
from carts import cart
from purchases import purchase

def call(userCpf):
  # Opções do usuário após listar o carrinho de compras
  def options(userCpf, cartList, finalValue):
    opt = input("\nEscolha uma opção:\n1 - Continuar comprando\n2 - Finalizar compra\n3 - Voltar ao menu\n")

    # Permite que o usuário continue adicionando itens ao carrinho
    if opt == '1':
      return productPurchase.call(userCpf)
    # Finaliza a compra com todos os produtos do carrinho
    if opt == '2':
      return purchase.checkout(userCpf, cartList, finalValue)
    # Volta ao menu principal
    elif opt == '3':
      return
    # Caso de erro
    else:
      print("\nPor favor, digite uma opção válida!")
      return options(userCpf, cartList, finalValue)

  items = cart.getAllByUserCpf(userCpf)

  # Retorna caso o usuário não possuir nenhum item no carrinho
  if len(items) == 0:
    return print("\nSeu carrinho está vazio!")

  # Recebe todos os produtos salvos
  products = product.getAll()
  cartList = []
  counter = 0
  finalValue = 0.0

  # Informa a quantidade de itens no carrinho
  print(f"\nCarrinho ({len(items)} itens):\n")

  # Lista os itens do carrinho
  for i in items:
    counter += 1

    for p in products:
      if i.userCpf == userCpf and i.productId == p.id:
        itemValue = round(int(i.quantity) * float(p.value), 2)
        finalValue += itemValue
        print(f"{counter} - {p.name}. Quantidade: {i.quantity}. Valor unitário: R${float(p.value):.2f}. Valor: R${(itemValue):.2f}")
        cartList.append(cart.build(i.userCpf, i.productId, i.quantity))

  # Apresenta o valor total do carrinho de compras
  print(f"\nValor total: R${round(finalValue, 2):.2f}")

  return options(userCpf, cartList, finalValue)

