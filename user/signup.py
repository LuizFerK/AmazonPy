from user import login, user

def options():
  opt = input('Opções:\n\n1 - Tentar novamente\n2 - Entrar no sistema\n')

  if opt == '1':
    return call()
  elif opt == '2':
    return login.call()
  else:
    print('Por favor, digite uma opção válida!')
    return options()

def call():
  name = input("\nDigite seu nome: ")
  email = input("Digite seu email: ")
  cpf = input("Digite seu cpf: ")
  password = input("Digite sua senha: ")

  res = user.create(name, email, cpf, password)

  if isinstance(res, str):
    print(res)
    return options()

  else:
    print(f"\nBem vindo(a) à AmazonPy, {res.name}!\n")

    return res