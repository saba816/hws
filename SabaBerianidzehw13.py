#1
# def w_file():
#     with open("new5.txt", "w") as file:
#         while True:
#             input_ = input("Enter string: ")
#             if input_.strip().lower() == "enough":
#                 break
#             file.write(input_ + "\n")
# if __name__ == "__main__":
#     w_file()

def add_info(new_info):
    if new_info.strip() != "enough":
        with open("new5.txt", "a") as file:
            file.write(new_info + "\n")

if __name__ == "__main__":
    while True:
        input_ = input("Enter info: ")
        add_info(input_)
        if input_.strip().lower() == "enough":
            break

#2
import os

def create_file(path, file_name):
    directory = os.path.join(path, file_name)
    
    try:
        with open(directory, "w") as file:
            print(f"file {file_name} created in {path}")
    except IOError:
        print("file creation failed")

def list_files_in_location(path):
    files = os.listdir(path)
    print(f"files list in {path}:")
    for file in files:
        print(file)

if __name__ == "__main__":
    location = input("enter folder location: ")
    file_name = input("enter file name: ")

    create_file(location, file_name)
    list_files_in_location(location)


#3