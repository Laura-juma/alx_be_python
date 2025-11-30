class BankAccount:
  def __init__(self, account_balance= 0):
    self.account_balance = account_balance
    self.last_transaction= None
    self.last_amount = None

  def deposit(self, amount):
    self.last_transaction = "deposit"
    self.last_amount = amount
    self.account_balance += amount
    return self.account_balance
  
  def withdraw(self, amount):
    self.last_amount = amount
    if self.account_balance < amount:
      self.last_transaction = "failed withdrawal"
      return False
    else:
      self.last_transaction = "successful withdrawal"
      self.account_balance -= amount
      return True, self.account_balance
    
  def display_balance(self):
    if self.last_transaction == "deposit":
      print(f"You deposited {self.last_amount}. New account balance is {self.account_balance}")
    elif self.last_transaction == "failed withdrawal":
      print(f"Insufficient funds")
    elif self.last_transaction == "successful withdrawal": 
      print(f"You withdrew {self.last_amount}. New account balance is {self.account_balance}")
    else:
      print(f"Your balance is {self.account_balance}")

  
          
  

    
