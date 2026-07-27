class BankAccounr:

    __balance =0

    #deposite
    def deposit(self,amount):

        if amount > 0:
            self.__balance += amount
            print("sucessfully desposit")

        else:
            print("invalid amount")



    #cash/withdraw

    def withdraw(self, amount):
        if amount>0 and amount<= self.__balance:
            self.__balance -= amount

            print("withdraw success")

        else:
            print("insufficiant balance")


    #check

    def checkBalance(self):

        return self.__balance



obj = BankAccounr()

obj.deposit(500)
print(obj.checkBalance())

obj.withdraw(600)
print(obj.checkBalance())
