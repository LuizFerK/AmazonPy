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
  flag = ''

  with open('users.csv','r') as file:
    for row in file:
      bdName, bdEmail, bdCpf, bdPassword = row.replace('\n', '').split(', ')

      if email == bdEmail:
        flag = 'Email já cadastrado'
      elif cpf == bdCpf:
        flag = 'Cpf já cadastrado'
      else:
        flag = ''

  if flag == '':
    with open('users.csv','a') as fs:
      fs.write(f"{user.name}, {user.email}, {user.cpf}, {user.password}\n")

    return user
  else:
    return flag
