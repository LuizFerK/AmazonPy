from user import user

def call():
  matchUser = user.build('', '', '', '')
  matchEmail = input("Digite seu email: ")
  matchPassword = input("Digite sua senha: ")
  res = ''

  with open('databases/users.csv','r') as file:
    for row in file:
      name, email, cpf, password = row.replace('\n', '').split(', ')

      if matchEmail != email or matchPassword != password:
        res = 'Usuário ou senha incorretos, tente novamente\n'
      else:
        res = ''
        matchUser = user.build(name, email, cpf, password)
        break

    if res == '':
      print(f"\nBem vindo(a) à AmazonPy, {matchUser.name}!\n")

      return matchUser
    else:
      print(res)
      return call()