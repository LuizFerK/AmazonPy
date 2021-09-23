from users import user as userModel

def call(userCpf):
  # Modifica o saldo do usuário
  def add(userBalance):
    try:
      value = float(input("\nDigite o valor do depósito:\n\nR$"))

      # Caso de erro
      if value < 1:
        print("\nPor favor, digite um valor válido.")
        add(userBalance)
      # Caso o usuário passe do limite de depósito estipulado
      elif value > 2000:
        print("\nO valor máximo de depósito é de R$2000.00")
        add(userBalance)
      # Caso de sucesso
      else:
        userModel.updateUserBalance(userCpf, value + userBalance)
        print(f"\nSaldo de R${round(value, 2):.2f} adicionado a conta com sucesso!\nSeu saldo atual é de R${round(value + userBalance, 2):.2f}")
    # Caso de erro de formatação do valor de depósito
    except:
      print("\nPor favor, digite um valor válido.")
      add()

  # Permite o usuário saber seu saldo e escolher entre depositar ou retornar ao menu principal
  def options(userBalance):
    opt = input(f"\nSeu saldo atual é de R${user.balance:.2f}. Deseja adicionar saldo a sua conta?\n1 - Sim. Adicionar saldo\n2 - Não. Retornar ao menu principal\n")

    if opt == '1':
      return add(userBalance)
    elif opt == '2':
      return
    else:
      print("\nPor favor, digite uma opção válida!")
      return options(userBalance)

  user = userModel.getByCpf(userCpf)

  return options(user.balance)