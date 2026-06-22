class Bank:
    def __init__ (self,acct_name,acct_number,current_amt=10000):
        self.acct_name = acct_name
        self.acct_number = acct_number
        self.current_amt = current_amt
    def __repr__(self):
        return f"Bank: '{self.acct_name}',{self.acct_number}, {self.current_amt}"
    def deposit(self,amt_added):
        self.current_amt += amt_added
        print(f"your current balance is ${self.current_amt}")
    def withdraw(self, amt_removed):
        if self.current_amt < amt_removed:
            print("INSUFFICIENT FUNDS")
        elif amt_removed < 0:
            print("Invalid amount")
        else:
            if self.current_amt < 0:
                print ("INSUFFICIENT FUNDS")
            else:
                self.current_amt-=amt_removed
                print(f"your current balance is ${self.current_amt}")
            
    def transfer(self, recipient, amount):
        if self.current_amt < amount:
            print ('INSUFFICIENT FUNDS')
        elif amount < 0:
            print("Invalid amount")
        else:
            if self.current_amt < 0:
                print ("INSUFFICIENT FUNDS")
            else:
                self.current_amt -= amount 
                recipient.current_amt+=amount
                print (f"you have sent ${amount} to {recipient.acct_name}, now have ${self.current_amt} and {recipient.acct_name} has ${recipient.current_amt}")
