class Product:
  id = 0
  name = ''
  value = 0.0

# Builda um produto
def build(id, name, value):
  product = Product()
  product.id = id
  product.name = name
  product.value = value

  return product

# Retorna todos os produtos salvos
def getAll():
  products = []

  with open('databases/products.csv','r') as file:
    for row in file:
      id, name, value = row.replace('\n', '').split(', ')

      products.append(build(id, name, value))

  return products
