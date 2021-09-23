class User:
  name = ''
  email = ''
  cpf = ''
  password = ''
  balance = 0.0

def build(name, email, cpf, password, balance):
  user = User()
  user.name = name
  user.email = email
  user.cpf = cpf
  user.password = password
  user.balance = balance

  return user

def create(name, email, cpf, password, balance):
  cpf = cpf.replace('.', '').replace('-', '')
  user = build(name, email, cpf, password, balance)
  flag = ''

  with open('databases/users.csv','r') as file:
    for row in file:
      bdName, bdEmail, bdCpf, bdPassword, bdBalance = row.replace('\n', '').split(', ')

      print(bdCpf, cpf)

      if email == bdEmail:
        flag = 'Email já cadastrado'
      elif cpf == bdCpf:
        flag = 'Cpf já cadastrado'
      else:
        flag = ''

  if flag == '':
    with open('databases/users.csv','a') as fs:
      fs.write(f"{user.name}, {user.email}, {user.cpf}, {user.password}, {user.balance}\n")

    return user
  else:
    return flag

def getByCpf(userCpf):
  matchUser = build('', '', '', '', 0.0)

  with open('databases/users.csv','r') as file:
    for row in file:
      name, email, cpf, password, balance = row.replace('\n', '').split(', ')

      if cpf == userCpf:
        matchUser = build(name, email, cpf, password, float(balance))
        break
  
  return matchUser

def updateUserBalance(userCpf, newBalance):
  users = []

  with open('databases/users.csv','r') as file:
    for row in file:
      name, email, cpf, password, balance = row.replace('\n', '').split(', ')

      if cpf == userCpf:
        users.append(f"{name}, {email}, {cpf}, {password}, {round(newBalance, 2)}\n")
      else:
        users.append(f"{name}, {email}, {cpf}, {password}, {balance}\n")
  
  with open('databases/users.csv','w') as file:
    file.write(''.join(users))