expenses= []
while True:
  print("\n1.Aggiungi spesa")
  print("2. Visualizza totale")
  print("3. Esci")

choice= input( "Scelta: ")
if choice== "1":
  name= input("Nome espesa: ")
  amount= float(input(" Importo: "))
  expenses.append((name,amount))
  print("Spesa aggiunta")
elif choice == 2:
  total= sum(amount for _,amount in expenses)
  print("Totale spese:{total}£")
elif choice== 3:
  break
else:
  print("Scelta non valida")
