from users import login, signup, user, addBalance
from products import purchase
from carts import checkout
from purchases import purchaseList

# Inicializa o controle de usuário com um usuário vazio
user = user.build('', '', '', '', 0.0)

print("Bem vindo(a) à AmazonPy!")

def menu(user):
  # Verifica se o usuário está logado e disponibiliza as opções válidas
  if user.name != '':
    opt = input("\nEscolha uma das opções abaixo para continuar:\n1 - Ver produtos\n2 - Ver carrinho\n3 - Ver compras\n4 - Adicionar saldo\n0 - Sair\n")
  else:
    opt = input("\nÉ novo por aqui? Escolha uma das opções abaixo:\n1 - Sim, sou novo na AmazonPy. Realizar cadastro\n2 - Já sou cliente. Entrar\n0 - Sair\n")

  if user.name != '':
    # Sai do app
    if opt == '0':
      return
    # Permite o usuário verificar os produtos da loja
    elif opt == '1':
      purchase.call(user.cpf)
      menu(user)
    # Permite o usuário verificar o itens que adicionou ao carrinho
    elif opt == '2':
      checkout.call(user.cpf)
      menu(user)
    # Lista todas as compras do usuário
    elif opt == '3':
      purchaseList.call(user.cpf)
      menu(user)
    # Permite que o usuário adicione saldo a sua conta
    elif opt == '4':
      addBalance.call(user.cpf)
      menu(user)
    # Caso de erro
    else:
      print("Por favor, digite uma opção válida!")
      menu(user)
  else:
    # Realiza o cadastro de um novo usuário
    if opt == '1':
      user = signup.call()
      menu(user)
    # Permite que um usuário já existente logue em sua conta
    elif opt == '2':
      user = login.call()
      menu(user)
    # Sai do app
    elif opt == '0':
      return
    # Caso de erro
    else:
      print("\nPor favor, digite uma opção válida!\n")
      menu(user)

menu(user)