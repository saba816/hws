# # merge sort

# # დავაგენერიროთ რაიმე ცვლადი randint ფუნქციის მეშვეობით
# import random

# def generate_random_arr(length, min, max):
#     return [random.randint(min, max) for _ in range(length)]

# # შევქმნათ ფუნქცია
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     # გავყოთ arr ორ ნაწილად
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     # რეკურსიულად ვასორტირებთ\ვყოფთ ორ ნახევარს
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)

#     # ვაერთიანებთ ორ ნახევარს
#     return merge(left_half, right_half)

# # ვქმნით ფუნქციას სადაც შევინახავთ left და right ნახევრებს
# def merge(left, right):
#     result = []
#     i = j = 0

# # ვანაწილებთ ორ ნახევარს, left-ში აღებულ რიცხვზე ნაკლები, right-ში რიცხვის ტოლი და მეტი
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

# # ვაერთიანებთ დასორტირებულ ვარიანტს
#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# # მაგალითი
# random_arr = generate_random_arr(1000, 1, 1000000)
# print("Unsorted array:", random_arr)

# sorted_arr = merge_sort(random_arr)
# print("Sorted array:", sorted_arr)
