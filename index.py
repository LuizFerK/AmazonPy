from users import login, signup, user
from products import purchase

# To-do

# * Validações de email, cpf e senha
# * Testes gerais
# * Iniciar domínio de compras

user = user.build('', '', '', '')

print("Bem vindo(a) à AmazonPy!")

def menu(user):
  if user.name != '':
    opt = input("\nEscolha uma das opções abaixo para continuar:\n1 - Ver produtos\n2 - Ver carrinho\n3 - Pagar conta\n0 - Sair\n")
  else:
    opt = input("\nÉ novo por aqui? Escolha uma das opções abaixo (1 ou 2):\n1 - Sim. Realizar cadastro\n2 - Não. Entrar\n0 - Sair\n")

  if user.name != '':
    if opt == '1':
      purchase.call()
      menu(user)
    elif opt == '2':
      print("carrinho")
    elif opt == '0':
      return
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
    elif opt == '0':
      return
    else:
      print("\nPor favor, digite uma opção válida!\n")
      menu(user)

menu(user)