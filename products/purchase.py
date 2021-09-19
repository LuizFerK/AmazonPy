from products import product

def call():
  def error():
    print("Por favor, digite valores válidos!")
    return call()

  def options():
    final_opt = input("\nDeseja continuar comprando?\n1 - Sim\n2 - Não. Retornar ao menu principal\n")

    if final_opt == '1':
      return call()
    elif final_opt == '2':
      return
    else:
      print("Por favor, digite uma opção válida!")
      return options()

  products = product.getAll()

  print("\nProdutos disponíveis:\n")

  for p in products:
    print(f"{p.id} - {p.name}: R${float(p.value):.2f}")

  opt = input("Digite o número do produto e a quantidade que deseja comprar!\n(Para sair, digite 0)\n")

  if opt == '0':
    return
    
  try:
    productId, quantity = map(int, opt.split())

    if productId < 1 or productId > 20 or quantity < 1:
      return error()

    print("salvar")
    
    return options()
  except:
    return error()
