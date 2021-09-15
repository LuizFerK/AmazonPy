from user import user

def call():
  name = input("\nDigite seu nome: ")
  email = input("Digite seu email: ")
  cpf = input("Digite seu cpf: ")
  password = input("Digite sua senha: ")

  newUser = user.create(name, email, cpf, password)

  print(f"\nBem vindo(a) à AmazonPy, {newUser.name}!\n")

  return newUser