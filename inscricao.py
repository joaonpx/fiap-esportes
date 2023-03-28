print("\n   FIAP Esportes - Inscrição\n")

class StudentInfo():
   em = input("Por favor, digite seu RM: ")
   name = input("Por favor, digite seu nome completo: ")
   age = input("Por favor, digite sua idade: ")

student = StudentInfo()

# verificando se o rm é realmente um digito
if student.em.isdigit() == False:
   print("\nRM invalido, tente novamente.")

   quit()

# verificando tamanho do rm
elif len(str(student.em)) != 6:
   print("\nRM invalido, tente novamente.")

   quit()

# verificando se o estudante tem mais de 18 anos
if int(student.age) >= 18:
  print(f"\n{student.name.split()[0]}, sua participação foi autorizada.")
  print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")
  
else:
  authorized = input("Você possui autorização dos responsáveis para participar? S - SIM ou N - NÃO: ")

  #verificando se o estudante tem autorização dos responsáveis
  if authorized.upper() == 'S':
      print(f"\n{student.name.split()[0]}, sua participação foi autorizada.")
      print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")

  else:
    print("\nSua participação não foi autorizada por causa da sua idade.")
