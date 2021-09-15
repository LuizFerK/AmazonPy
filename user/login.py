from user import user

def call():
  matchUser = user.build('', '', '', '')
  matchEmail = input("\nDigite seu email: ")
  matchPassword = input("Digite sua senha: ")

  with open('users.csv','r') as file:
    flag = 0

    for row in file:
      name, email, cpf, password = row.replace('\n', '').split(', ')

      if matchEmail != email or matchPassword != password:
        flag = 1
      else:
        flag = 0
        matchUser = user.build(name, email, cpf, password)
        break

  if flag == 0:
    print(f"\nBem vindo(a) à AmazonPy, {matchUser.name}!\n")

    return matchUser
  else:
    print("Usuário ou senha incorretos, tente novamente")
    return call()