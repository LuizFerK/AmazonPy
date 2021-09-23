class Cart:
  userCpf = ''
  productId = ''
  quantity = 0

# Builda um item do carrinho de compras
def build(userCpf, productId, quantity):
  cart = Cart()
  cart.userCpf = userCpf
  cart.productId = productId
  cart.quantity = quantity

  return cart

# Adiciona um novo item ao carrinho de compras
def add(userCpf, productId, quantity):
  item = build(userCpf, productId, quantity)

  with open('databases/carts.csv','a') as fs:
    fs.write(f"{userCpf}, {productId}, {quantity}\n")

  print(f"\n{quantity} unidade(s) do produto de número {productId} foram adicionadas ao carrinho!")

  return item

# Retorna o carrinho de compras de um usuário com base em seu CPF
def getAllByUserCpf(userCpf):
  items = []

  with open('databases/carts.csv','r') as file:
    for row in file:
      bdUserCpf, productId, quantity = row.replace('\n', '').split(', ')

      if bdUserCpf == userCpf:
        items.append(build(userCpf, productId, quantity))

  return items

# Remove todos os itens do carrinho de um usuário (usado ao final de uma compra)
def deleteAllByUserCpf(userCpf):
  items = []

  with open('databases/carts.csv','r') as file:
    for row in file:
      bdUserCpf, productId, quantity = row.replace('\n', '').split(', ')

      if bdUserCpf != userCpf:
        items.append(f"{bdUserCpf}, {productId}, {quantity}\n")

  with open('databases/carts.csv','w') as file:
    file.write(''.join(items))