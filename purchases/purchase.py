def checkout(items):
  with open('databases/purchases.csv','a') as fs:
    for i in items:
      fs.write(f"{i.userCpf}, {i.productId}, {i.quantity}\n")