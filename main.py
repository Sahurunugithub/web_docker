
a = [1,2,3,2,1]
c = a.copy()
c.reverse()
if a==c:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")

#
# class Amount:
#     def __init__(self,balance, accno):
#         self.bal= balance
#         self.acc= accno
#
#     def debit(self,amount):
#         self.bal -= amount
#         print("The debited amount is ",amount)
#         print("the total balance is ", self.total_balance())
#
#     def credit(self,amount):
#         self.bal += amount
#         print("The credited amount is ",amount)
#         print("the total balance is ",self.total_balance())
#
#     def total_balance(self):
#         return self.bal
#
# acc1 = Amount(35000, 123)
# print(acc1.bal)
# print(acc1.acc)
#
# debit_=int(input("Enter the amount you want to debit: "))
# acc1.debit(debit_)
#
# credit_=int(input("Enter the amount you want to credit: "))
# acc1.credit(credit_)
#
#
