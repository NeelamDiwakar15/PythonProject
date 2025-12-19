balance=10000
def check_balance():
    return balance
def deposit(amount):
   if (amount>0):
      print("Deposit successful")
      global balance
      balance+=amount
   else:
      print(f"Inavlid amount :{amount}")
   return balance
def withdraw(amount_draw):
   global balance
   if (amount_draw>0 and balance>0):
      print("withdraw successful")
      balance-=amount_draw
   else:
      print(f"Inavlid amount :{amount_draw}")
   return balance

while(True):
  choice=int(input("\n1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit \nchoose: "))
  if choice==1:
     print("\tBalance is :",check_balance())
  elif choice==2:
     amount=int(input("enter Deposit_amount: ")) 
     print("\tBalance is: ",deposit(amount))
  elif choice==3:
      amount_draw=int(input("enter withDraw_amount: ")) 
      print("\tBalance is :",withdraw(amount_draw))
  elif choice==4:
     print("\tEXIT")
     break
  else:
     print("Invalid choice ,choose again🎈")
    
