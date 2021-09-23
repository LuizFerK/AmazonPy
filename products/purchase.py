from products import product
from carts import cart, checkout

def call(userCpf):
  # Caso de erro
  def error():
    print("Por favor, digite valores válidos!")
    return call(userCpf)

  # Opções do usuário após adicionar um produto ao carrinho
  def options():
    final_opt = input("\nDeseja continuar comprando?\n1 - Sim\n2 - Não. Visualizar carrinho de compras\n3 - Não. Retornar ao menu principal\n")

    if final_opt == '1':
      return call(userCpf)
    elif final_opt == '2':
      return checkout.call(userCpf)
    elif final_opt == '3':
      return
    else:
      print("Por favor, digite uma opção válida!")
      return options()

  # Retorna todos os produtos cadastrados
  products = product.getAll()

  print("\nProdutos disponíveis:\n")

  # Lista os produtos em tela
  for p in products:
    print(f"{p.id} - {p.name}: R${float(p.value):.2f}")

  # Pede ao usuário qual item ele deseja adicionar ao carrinho
  opt = input("Digite o número do produto e a quantidade que deseja comprar!\n(Para sair, digite 0)\n")

  if opt == '0':
    return
    
  # Salva o produto e a quantidade desejada e retorna erro em caso de formatação inválida
  try:
    productId, quantity = map(int, opt.split())

    if productId < 1 or productId > 20 or quantity < 1:
      return error()

    cart.add(userCpf, productId, quantity)
    
    return options()
  except:
    return error()
