import random
class Atm(object):
    def __init__(self,cardNumber, pin,userName):
        self.cardNumber = cardNumber
        self.pin = pin
        self.userName = userName

    def cashWithdrawal(self):
        withdrawalMoney = input("How much money do you want to withdraw? ")
        print("Withdrawing "+withdrawalMoney+" rupees...")
        print("Successfully withdrawed "+withdrawalMoney+" rupees")

    def balanceEnquiry(self):
        currentBalance = str(random.randint(100000,550000))
        print("Your current account balance is "+currentBalance+" rupees")


bankAccount = Atm("864597135","9834","Yashas Jain")
atmOperations = input("Do you want to withdraw money or or check your account balance? ")
 
if(atmOperations == "Withdraw"):
    bankAccount.cashWithdrawal()

elif(atmOperations == "Account Balance"):
    bankAccount.balanceEnquiry()

