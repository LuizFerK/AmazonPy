import signup

global isLogged
isLogged = False

def menu():
  print("Bem vindo(a) à AmazonPy!\n")

  if isLogged:
    opt = int(input("Escolha uma das opções abaixo para continuar:\n1 - Ver produtos\n2 - Ver carrinho\n3 - Pagar conta\n"))
  else:
    opt = int(input("É novo por aqui? Escolha uma das opções abaixo (1 ou 2):\n1 - Sim. Realizar cadastro\n2 - Não. Entrar\n"))

  if isLogged:
    if opt == 1:
        print("comprar")
    elif opt == 2:
        print("carrinho")
    elif opt == 3:
        print("conta")
    else:
      print("Por favor, digite uma opção válida!")
      menu()
  else:
    if opt == 1:
      signup.call()
    elif opt == 2:
      print("login")
    else:
      print("Por favor, digite uma opção válida!")
      menu()

menu()