from users import user

def call():
  # Requisita o email e a senha do usuário
  matchUser = user.build('', '', '', '', 0.0)
  matchEmail = input("\nDigite seu email: ")
  matchPassword = input("Digite sua senha: ")
  res = 'empty'

  # Verifica se o usuário existe e se sua senha está correta
  with open('databases/users.csv','r') as file:
    for row in file:
      name, email, cpf, password, balance = row.replace('\n', '').split(', ')

      if matchEmail != email or matchPassword != password:
        res = '\nUsuário ou senha incorretos, tente novamente'
      else:
        res = ''
        matchUser = user.build(name, email, cpf, password, balance)
        break
      
    if res == 'empty':
      print("\nUsuário não encontrado, por favor, realize o cadastro")
      
      return matchUser
    # Retorna o usuário em caso de sucesso
    if res == '':
      print(f"\nBem vindo(a) à AmazonPy, {matchUser.name}!")

      return matchUser
    # Em caso de erro, retorna o erro e permite uma nova tentativa de login
    else:
      print(res)
      return call()