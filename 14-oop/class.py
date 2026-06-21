class Chai:
    pass #pass normal khali jagah hota hai 

class ChaiTime:
    pass

ginger_tea = Chai() #initalize
print(type(ginger_tea)) #<class '__main__.Chai'>
print(type(ginger_tea) is Chai) #True
print(type(ginger_tea) is ChaiTime) #False


#Constructor

# class Student:
#     def __init__(self, name, course):  #Constructor
#         self.name = name #Attribute
#         self.course = course #Attribute
#     def printValues(self): #Method
#         print(f"{self.name} {self.course}")


# student = Student("Ali", "Python")
# print("Name:", student.name)
# print("Course:", student.course)


#inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Person: {self.name}"


class Student(Person): #Inherit
    pass


student = Student("Ali")
print(student.describe())


#Encapsulation

class FeeAccount:
    def __init__(self, balance):
        self._balance = balance # _ variable ya attribute private for this class

    def pay(self, amount):
        if amount <= 0:
            return "Invalid payment"
        self._balance = max(0, self._balance - amount)
        return "Payment accepted"

    def get_balance(self):
        return self._balance


account = FeeAccount(5000)
# account._balance
print(account.pay(2000))
print("Balance:", account.get_balance())


#Polymorphism

class EmailNotification:
    def send(self):
        return "Email sent"


class SmsNotification:
    def send(self):
        return "SMS sent"


notifications = [EmailNotification(), SmsNotification()]
for notification in notifications:
    print(notification.send())

#ek hi common method send() dono me use hora hai

#Different objects can respond to the same method name in their own way.