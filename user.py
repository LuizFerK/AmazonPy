class User:
  name = ''
  email = ''
  cpf = ''
  password = ''

def create(name, email, cpf, password):
  user = User()
  user.name = name
  user.email = email
  user.cpf = cpf
  user.password = password

  with open('users.csv','a') as fs:
    fs.write(f"{user.name}, {user.email}, {user.cpf}, {user.password}\n")

  return user