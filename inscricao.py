print("\n   FIAP Esportes - Inscrição\n")

em = int(input("Por favor, digite seu RM: "))
age = int(input("Por favor, digite sua idade: "))

if age >= 18:
  print(f"\nSua participação foi autorizada, aluno de RM: {em}")
  print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")
else:
  authorized = input("Você possui autorização dos responsáveis para participar? S - SIM ou N - NÃO: ")

  if authorized == 'S':
      print(f"\nSua participação foi autorizada, aluno de RM: {em}")
      print("Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!")

  else:
    print("\nSua participação não foi autorizada por causa da sua idade.")
