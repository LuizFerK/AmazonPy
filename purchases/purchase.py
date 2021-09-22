from carts import cart

def checkout(userCpf, items, finalValue):
  def options():
    opt = input("Seu saldo é insuficiente para finalizar a compra. Deseja adicionar mais saldo a sua conta?\n1 - Sim. Adicionar saldo\n2 - Não. Retornar ao menu principal")
    
    if opt == '1':
      return print('balance')
    elif opt == '2':
      return
    else:
      print("\nPor favor, digite uma opção válida!")
      return options()

  def comparePasswords(userPassword):
    def wrongPasswordOptions():
      opt = input("\nSenha incorreta, deseja tentar novamente?\n1 - Sim. Tentar novamente\n2 - Não. Voltar ao menu principal\n")

      if opt == '1':
        return comparePasswords(userPassword)
      elif opt == '2':
        return False
      else:
        print("\nPor favor, digite uma opção válida!")
        return wrongPasswordOptions()

    password = input("\nPara concluir a compra, por favor, digite sua senha:\n")

    if password != userPassword:
      return wrongPasswordOptions()
    else:
      return True


  balance = 1200.00
  password = 'asd123'
  print(f"\nO valor total da sua compra é de R${finalValue:.2f} e seu saldo atual é de R${balance:.2f}")

  if balance < finalValue:
    return options()

  if comparePasswords(password):
    with open('databases/purchases.csv','a') as fs:
      for i in items:
        fs.write(f"{userCpf}, {i.productId}, {i.quantity}\n")

    cart.deleteAllByUserCpf(userCpf)

    print("\nCompra finalizada com sucesso. Obrigado(a) por comprar na AmazonPy!")

  