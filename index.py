from user import login, signup, user

user = user.build('', '', '', '')

print("Bem vindo(a) à AmazonPy!\n")

def menu(user):
  if user.name != '':
    opt = input("Escolha uma das opções abaixo para continuar:\n1 - Ver produtos\n2 - Ver carrinho\n3 - Pagar conta\n")
  else:
    opt = input("É novo por aqui? Escolha uma das opções abaixo (1 ou 2):\n1 - Sim. Realizar cadastro\n2 - Não. Entrar\n")

  if user.name != '':
    if opt == '1':
        print("comprar")
    elif opt == '2':
        print("carrinho")
    elif opt == '3':
        print("conta")
    else:
      print("Por favor, digite uma opção válida!")
      menu(user)
  else:
    if opt == '1':
      user = signup.call()
      menu(user)
    elif opt == '2':
      user = login.call()
      menu(user)
    else:
      print("\nPor favor, digite uma opção válida!\n")
      menu(user)

menu(user)