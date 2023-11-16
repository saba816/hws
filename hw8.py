# 1
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111, 123, 412, 65231]
# a = int(input("Enter a number: "))

# multiply = lambda x: x * a

# result = list(filter(lambda x: True, map(multiply, li)))

# print("Original List:", li)
# print(f"List multiplied by {a}:", result)

# 2
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111, 123, 412, 65231, "asdfg", "Asdfg", "qwerty", "Qwerty", "pointless", "Aizen"]
# count1 = len(li)

# filtered_list = [item for item in li if isinstance(item, str) and item[0].isupper()] 

# count2 = len(filtered_list)

# print("Count of list members:", count1)
# print("Count of Non-Lowercase Members:", count2)

# 3
# li = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -111, 123, -412, 65231]
# positive_count = len(list(filter(lambda x: x>0, li)))
# negative_count = len(list(filter(lambda x: x<0, li)))
# print("These are positive numbers in list:",positive_count, "and these are negative ones:", negative_count)

