class User:
  name = ''
  email = ''
  cpf = ''
  password = ''

def build(name, email, cpf, password):
  user = User()
  user.name = name
  user.email = email
  user.cpf = cpf
  user.password = password

  return user

def create(name, email, cpf, password):
  user = build(name, email, cpf, password)

  with open('users.csv','a') as fs:
    fs.write(f"{user.name}, {user.email}, {user.cpf}, {user.password}\n")

  return user