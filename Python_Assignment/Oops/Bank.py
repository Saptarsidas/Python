# Created a class representing a bank account which attributes like account number and account holder name and balance implement methods to deposit  and withdraw money from the account
class Bank:
    def __init__(self,acc_name,acc_no,balance):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.balance=balance
    def  deposit(self,amount):
        self.balance+=amount
        return (f"Deposited {amount} successfully. New balance is {self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return(f"withdraw {amount} successfully. New balance is {self.balance}")
        else:
            return "Insuficient Balance"
    def acct_info(self):
        return f"Account Name: {self.acc_name}\nAccount no: {self.acc_no}\nBalance: {self.balance}"
        
account=Bank("Saptarsi Das",101,5000000)
print(account.deposit(5000))
print(account.withdraw(500))
print(account.acct_info())

    


    