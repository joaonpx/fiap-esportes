print("\n   FIAP Esportes - Inscrição\n")

class StudentInfo():
   em = int(input("Por favor, digite seu RM: "))
   name = input("Por favor, digite seu nome completo: ")
   age = int(input("Por favor, digite sua idade: "))

student = StudentInfo()

# verificando tamanho do rm
if len(str(student.em)) is not 6:
   print("\nRM invalido, tente novamente.")

   quit()

# verificando se o estudante tem mais de 18 anos
if student.age >= 18:
  print(f"\n{student.name.split()[0]}, sua participação foi autorizada.")
  print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")
  
else:
  authorized = input("Você possui autorização dos responsáveis para participar? S - SIM ou N - NÃO: ")

  if authorized.upper() == 'S':
      print(f"\n{student.name.split()[0]}, sua participação foi autorizada.")
      print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")

  else:
    print("\nSua participação não foi autorizada por causa da sua idade.")
