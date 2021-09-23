from users import user, addBalance
from carts import cart

def checkout(userCpf, items, finalValue):
  # Opções do usuário caso seu saldo seja insuficiente para finalizar a compra
  def options():
    opt = input("\nSeu saldo é insuficiente para finalizar a compra. Deseja adicionar mais saldo a sua conta?\n1 - Sim. Adicionar saldo\n2 - Não. Retornar ao menu principal\n")
    
    # Permite que o usuário adicione saldo a sua conta
    if opt == '1':
      return addBalance.call(userCpf)
    # Permite que o usuário retorne ao menu principal
    elif opt == '2':
      return
    # Caso de erro
    else:
      print("\nPor favor, digite uma opção válida!")
      return options()

  def comparePasswords(userPassword):
    # Retorna erro caso a senha esteja errada e permite que o usuário tente novamente
    def wrongPasswordOptions():
      opt = input("\nSenha incorreta, deseja tentar novamente?\n1 - Sim. Tentar novamente\n2 - Não. Voltar ao menu principal\n")

      # Tenta novamente
      if opt == '1':
        return comparePasswords(userPassword)
      # Retorna ao menu
      elif opt == '2':
        return False
      # Caso de erro
      else:
        print("\nPor favor, digite uma opção válida!")
        return wrongPasswordOptions()

    # Pede a senha para finalizar a compra
    password = input("\nPara concluir a compra, por favor, digite sua senha:\n")

    # Compara a senha informada pelo usuário com sua senha de cadastro
    if password != userPassword:
      return wrongPasswordOptions()
    else:
      return True

  # Informa o valor total da compra do usuário
  purchaseUser = user.getByCpf(userCpf)
  print(f"\nO valor total da sua compra é de R${finalValue:.2f} e seu saldo atual é de R${purchaseUser.balance:.2f}")

  # Retorna erro caso o usuário não tenha saldo suficiente para completar a compra
  if purchaseUser.balance < finalValue:
    return options()

  # Pede a senha para o usuário e, caso esteja correta, salva e finaliza a compra
  if comparePasswords(purchaseUser.password):
    with open('databases/purchases.csv','a') as fs:
      for i in items:
        fs.write(f"{userCpf}, {i.productId}, {i.quantity}\n")

    cart.deleteAllByUserCpf(userCpf)
    user.updateUserBalance(userCpf, purchaseUser.balance - finalValue)

    print("\nCompra finalizada com sucesso. Obrigado(a) por comprar na AmazonPy!")

  