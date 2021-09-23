from users import login, user
from validators import userValidator

def call():
  # Opções do usuário em caso de erro
  def options():
    opt = input('Opções:\n\n1 - Tentar novamente\n2 - Entrar no sistema\n')

    # Permite uma nova tentativa de cadastro
    if opt == '1':
      return call()
    # Permite o login caso o usuário já exista
    elif opt == '2':
      return login.call()
    # Caso de erro
    else:
      print('Por favor, digite uma opção válida!')
      return options()

  name = input("\nDigite seu nome: ")
  email = input("Digite seu email: ")
  cpf = input("Digite seu cpf: ")
  password = input("Digite sua senha: ")

  # Valida os dados do cadastro
  validation = userValidator.validate(cpf, email, password)

  if validation != 0:
    print(validation)
    return call()

  res = user.create(name, email, cpf, password, 0.0)

  if isinstance(res, str):
    print(res)
    return options()

  else:
    print(f"\nBem vindo(a) à AmazonPy, {res.name}!\n")

    return res