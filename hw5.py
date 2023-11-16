#1
# consumers = []

# for i in range(3):
#     name = input("Enter user's name: ")
#     lastname = input("Enter user's lastname: ")
#     age = input("Enter user's age: ")

#     user_info = [name, lastname, age]

#     consumers.append(user_info)

# index = int(input("Enter the index of the consumer you want to retrieve (0, 1, or 2): "))

# if 0 <= index < len(consumers):
#     consumer = consumers[index]
#     print(f"Name: {consumer[0]}")
#     print(f"Lastname: {consumer[1]}")
#     print(f"Age: {consumer[2]}")
# else:
#     print("Invalid index. Please enter a valid index (0, 1, or 2).")

#2
# user_info = []
# username = input("Enter username: ")
# password = input("enter password: ")
# ur_info = [username, password]
# if len(password)>=8 and len(username)>0:
#     user_info.append(ur_info)
# else:
#     print("ur password is too  short or u should enter username ")

#3
# actors = [
#     {
#         "name": "Tom Hanks",
#         "age": 66,
#         "best_known_for": "Forrest Gump, Cast Away, Saving Private Ryan",
#     },
#     {
#         "name": "Meryl Streep",
#         "age": 72,
#         "best_known_for": "The Devil Wears Prada, Sophie's Choice, Kramer vs. Kramer",
#     },
#     {
#         "name": "Leonardo DiCaprio",
#         "age": 47,
#         "best_known_for": "Titanic, Inception, The Revenant",
#     },
#     {
#         "name": "Jennifer Lawrence",
#         "age": 32,
#         "best_known_for": "The Hunger Games series, Silver Linings Playbook, Winter's Bone",
#     },
#     {
#         "name": "Denzel Washington",
#         "age": 67,
#         "best_known_for": "Training Day, Glory, Malcolm X",
#     },
# ]

# def find_actor_info(actor_name):
#     for actor in actors:
#         if actor["name"].lower() == actor_name.lower():
#             print(f"Name: {actor['name']}")
#             print(f"Age: {actor['age']}")
#             print(f"Best Known For: {actor['best_known_for']}")
#             return
#     print(f"Actor '{actor_name}' not found in the list.")

# user_input = input("Enter the name of an actor: ")

# find_actor_info(user_input)
