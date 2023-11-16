#1
# from random import choice

# choice_list = ["rock", "scissors", "paper"]

# human_score = 0
# computer_score = 0
# winning_score = 3

# while human_score < winning_score and computer_score < winning_score:
#     computer_choice = choice(choice_list)

#     human_choice = input("Enter one of the following: rock / scissors / paper ").lower()

#     if human_choice in choice_list:
#         if human_choice == computer_choice:
#             print("It's a draw!")
#         elif (human_choice == 'rock' and computer_choice == 'scissors') or (human_choice == 'scissors' and computer_choice == 'paper') or (human_choice == 'paper' and computer_choice == 'rock'):
#             print('Human wins this round!')
#             human_score += 1
#         else:
#             print('Computer wins this round!')
#             computer_score += 1
#         print(f"Current Score - Human: {human_score}, Computer: {computer_score}")
#     else:
#         print("Invalid choice. Please choose from rock, scissors, or paper.")

# if human_score > computer_score:
#     print("Human wins the game!")
# else:
#     print("Computer wins the game!")

#2
# number = int(input("Enter a number: "))
#  # number2 = int(input("Enter second number: "))

# for i in range(1, number + 1):
#   # for j in range(1, number2 + 1):
#     for j in range(1, 11):
#         result = i * j
#         print(result, end=' ')
#     print()

#3
# bank_acc = 3000

# while True:
#     print(f"Current balance: {bank_acc} USD")
    
#     expense = int(input("Enter the expense amount (0 to stop): "))
    
#     if expense == 0:
#         print("Thank you for using the banking system. Goodbye!")
#         break

#     if expense > bank_acc:
#         print("You don't have enough money for this expense.")
#     else:
#         bank_acc -= expense
#         print(f"Expense of {expense} USD deducted from your account.")

# print(f"Final balance: {bank_acc} USD")

#4
# while True:
#     a = input("Enter something: ")
#     if a.lower() == 'quit':
#         break
#     else:
#         print("User Said Whaaat?!", end="  ")
#         print(f"User Said {a}")

# while True:
#     a = input("Enter something: ")
#     if a.lower() == 'quit':
#         break
#     else:
#         print("User Said Whaaat?!\nUser Said", a)
