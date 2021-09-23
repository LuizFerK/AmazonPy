from users import user

def call():
  matchUser = user.build('', '', '', '', 0.0)
  matchEmail = input("\nDigite seu email: ")
  matchPassword = input("Digite sua senha: ")
  res = ''

  with open('databases/users.csv','r') as file:
    for row in file:
      name, email, cpf, password, balance = row.replace('\n', '').split(', ')

      if matchEmail != email or matchPassword != password:
        res = 'Usuário ou senha incorretos, tente novamente'
      else:
        res = ''
        matchUser = user.build(name, email, cpf, password, balance)
        break

    if res == '':
      print(f"\nBem vindo(a) à AmazonPy, {matchUser.name}!")

      return matchUser
    else:
      print(res)
      return call()