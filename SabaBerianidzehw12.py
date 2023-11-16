#1
dct_a = {"first": "asd", "second": "asd", "third": "qwerty", "last": 123}
def unique_dict(dict1):
    unique_values = {}
    for key, value in dict1.items():
        if value not in unique_values.values():
            unique_values[key] = value
    return unique_values
print(unique_dict(dct_a))

#2
# dct_b = {}
# def check_dict(dict2):
#     return not bool(dict2)
# print(check_dict(dct_b))

dct_b = {}
def check_dict(dict2):
    if dict2 == {}:
        return True
    else:
        return False
print(check_dict(dct_b))

#3
adct = str(input("Enter a string: "))
def create_dict(dict3):
    created_dict = {}
    for i in dict3:
        if i in created_dict:
            created_dict[i] += 1
        else:
            created_dict[i] = 1
    return created_dict
print(create_dict(adct))

#4
def dict_to_list(dict4):
    return dict4.items()
print(dict_to_list(dct_a))