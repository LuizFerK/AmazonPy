import re

def validate(cpf, email, password):
  if not bool(re.match('[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}', cpf)):
    return 'O CPF informado está mal formatado'
  elif not bool(re.match('(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))', email)):
    return 'O email informado está mal formatado'
  elif len(password) < 6:
    return 'A senha deve ter mais de 6 caracteres'
  else:
    return 0
  