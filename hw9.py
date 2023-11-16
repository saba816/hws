# 1.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
# 2.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).
# 3.	დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.

#1
# lis = [3,1,23,123,653,0.2,12,3,11,2,41]
# lis.sort()
# print(lis)

#2
# lis = [3,1,23,123,653,0.2,12,3,11,2,41]
# sort_lis = sorted(lis, reverse=True)
# print(sort_lis)

#3
# import random
# import time

# def count_time(un):
#     arr1 = [random.randint(0, 1000) for _ in range(1000)]
#     arr2= [random.randint(0, 1000) for _ in range(2000)]
#     arr3 = [random.randint(0, 1000) for _ in range(3000)]
#     start_time1 = time.time() 
#     un(arr1)
#     end_time1 = time.time()
#     start_time2 = time.time()
#     un(arr2)
#     end_time2 = time.time()
#     start_time3 = time.time()
#     un(arr3)
#     end_time3 = time.time()
#     print('1k', end_time1 - start_time1, '2k', end_time2-start_time2,'3k',end_time3-start_time3)

# @count_time
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# @count_time
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]



# def generate_random_list(length):
#     return [random.randint(1, 1000) for _ in range(length)]

# #1k elements
# random_list_1k = generate_random_list(1000)

# #2k elements
# random_list_2k = generate_random_list(2000)

# #3k elements
# random_list_3k = generate_random_list(3000)

# time_bubble_1k = bubble_sort(random_list_1k.copy())
# time_selection_1k = selection_sort(random_list_1k.copy())

# time_bubble_2k = bubble_sort(random_list_2k.copy())
# time_selection_2k = selection_sort(random_list_2k.copy())

# time_bubble_3k = bubble_sort(random_list_3k.copy())
# time_selection_3k = selection_sort(random_list_3k.copy())

# print(f"1k elemets list - Bubble Sort: {time_bubble_1k:.6f} sec, Selection Sort: {time_selection_1k:.6f} sec")
# print(f"2k lements list - Bubble Sort: {time_bubble_2k:.6f} sec, Selection Sort: {time_selection_2k:.6f} sec")
# print(f"3k elements list - Bubble Sort: {time_bubble_3k:.6f} sec, Selection Sort: {time_selection_3k:.6f} sec")
