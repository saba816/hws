#1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def circle_area(self):
#         return 3.14 * self.radius**2
    
#     def circle_perimeter(self):
#         return 2 * 3.14 * self.radius
    
# circle1 = Circle(5)
# c1area = circle1.circle_area()
# c1perimeter = circle1.circle_perimeter()
# print(f"Circle are - {c1area}, perimeter - {c1perimeter}")

#2
# class Calculator:
#     def __init__(self, n1, n2):
#         self.n1=n1
#         self.n2=n2

#     def addition(self,n1,n2):
#         return n1+n2
    
#     def substraction(self,n1,n2):
#         return n1-n2
    
#     def multiplication(self,n1,n2):
#         return n1*n2
    
#     def division(self,n1,n2):
#         if n2 != 0:
#             return n1/n2
#         else:
#             return "You can't divide by zero"
    
# calc1 = Calculator(1,2)
# print(calc1.addition)

#3
# class Shopping:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product_name, price):
#         self.products.append({"name": product_name, "price": price})
#         print(f"{product_name} added product")

#     def remove_product(self, product_name):
#         for product in self.products:
#             if product["name"] == product_name:
#                 self.products.remove(product)
#                 print(f"{product_name} product removed")
#                 break
#         else:
#             print(f"{product_name} wasn't found in basket")

#     def display_cart(self):
#         total_price = sum(product["price"] for product in self.products)
#         print("Products in basket: ")
#         for product in self.products:
#             print(f"{product['name']} - {product['price']} GEl")
#         print(f"Total price {total_price} GEL")

# basket = Shopping()

# basket.add_product("1kg meat", 15)
# basket.add_product("ciggarets", 8)
# basket.add_product("toy gun", 50)

# basket.display_cart()

# basket.remove_product("1kg meat")

# basket.display_cart()

#4
# class BankAcc:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} GEl added to the balance, final balance: {self.balance} GEl")
#         else:
#             print("Error: your balance is lower than 0")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} GEl withdrawed, final balance: {self.balance} GEL")
#         else:
#             print("Error: you don't have enough money")

#     def display_balance(self):
#         print(f"{self.account_holder} account balance: {self.balance} GEL")

# account1 = BankAcc(account_holder="George", balance=1200)

# account1.display_balance()

# account1.deposit(700)
# account1.withdraw(150)
# account1.withdraw(1250)
