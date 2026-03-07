# Create a class BankAccount where the balance is a private attribute (use __balance).
# Write a deposit(amount) method.
# Write a withdraw(amount) method that only allows the withdrawal if there are enough funds.
# Write a get_balance() method to securely view the balance.
# Challenge: Try to change the balance directly from outside the class (e.g., account.__balance = 1000000) and see if it works!

class BankAccount:
    def __init__(self,balance,pin):
        self.__pin = pin
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print("Amount has been successfully deposited.")

    def withdraw(self,amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            print("Amount has been successfully withdrawn.")
            ch = input("Do you wish to see your remaining balance? ( y / n ) : ")
            while ch.lower() not in ['y' ,'n']:
                ch = input("Invalid input! Choose 'y' for yes and 'n' for no. : ")
            if ch.lower() == 'y': # Use .lower() here too!
                self.get_Balance(self.__pin) # Reuse your existing method
            else:
                print("Thankyou for using us!")
        else:
            print("Insufficient Balance! Cannot withdraw!")
    def get_Balance(self,pin):
        if self.__pin == pin:
            print(f"Balance : {self.__balance}")
        else:
            print("Invalid PIN. Cannot access balance. Please Try again.")            

b1 = BankAccount(20000,1234)
b1.__balance = 200
# b1.get_Balance(1234)
# b1.deposit(2000)
b1.withdraw(200)