from collections import defaultdict

menu = {
    'ხინკალი': 1, 'აჭარული ხაჭაპური': 8.5, 'ქაბაბი': 3.5, 'კარტოფილი ფრი': 4, 'მწვადი(1 შამფური)': 6, 'იმერული ხაჭაპური': 4, 'ლობიანი': 4, 
    'წყალი': 0.7, 'ლიმონათი': 3, 'ლუდი': 4, 'ცეზარი': 6, 'შემწვარი გოჭი': 8, 'ფხალი': 5
}

kkeys = list(menu.keys())

print("Menu: ")
for i, key in enumerate(kkeys):
    print(i+1, key, menu[key])

total_price = 0
orders = defaultdict(int)

while True:
    try:
        order = int(input(f"Enter meal number (1-{len(kkeys)}) (0 to end order): "))
        if order == 0:
            print("Order ended")
            break
        elif order in range(1, len(kkeys)+1):
            meals_ordered = kkeys[order-1]
            mnumber = int(input("Enter number of meals: "))
            if mnumber <= 0:
                print("That can't be number of meals! Try again! ")
                continue
            orders[meals_ordered] += mnumber * menu[meals_ordered]
            total_price += mnumber * menu[meals_ordered]
    except:
        print("Order failed! try again! ")

print("Order: ")
for key, value in orders.items():
    print(f"{key} number: {value/menu[key]} cost:{value} gel. ")
print("Total price:", total_price,"gel")

import os
import shutil

def create_executable(script_name):
    try:
        script_path = os.path.abspath(__file__)
        shutil.copy(script_path, script_name + "_exe.py")
        shutil.make_archive(script_name, 'zip', script_name + "_exe")
        shutil.move(script_name + ".zip", script_name + ".exe")
        shutil.rmtree(script_name + "_exe")
        print("Executable created successfully!")
    except Exception as e:
        print(f"Error creating executable: {e}")

create_executable('your_script_name')