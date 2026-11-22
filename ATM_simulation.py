def show_balance():
    print(f"Your balance is ${balance:.2f}")
def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount <=0:
        print("That's not a valid amount.")
        return 0
    else:
        return amount
    
def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))
    if amount <=0:
        print("That's not a valid amount.")
        return 0
    elif amount > balance:
        print("Insufficient funds!")
        return 0 
    else:
        return amount
    
balance = 0
is_running = True
while is_running:
    print("\n...Banking program...")
    print("1.Show Balance")    
    print("2.Deposit")
    print("3.Withdraw")   
    print("4.Exit")
    Choice = input("Enter your choice(1-4): ")
    if Choice == "1":
        show_balance()
    elif Choice == "2":
        balance +=deposit()
    elif Choice == "3":
        balance -=withdraw()
    elif Choice == "4":
        is_running = False
    else:
        print("Invalid Choice!")

print("Thanks! have a good day...")
