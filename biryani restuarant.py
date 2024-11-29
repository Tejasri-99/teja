'''print("Welcome to Ammu's panipuri center")

menu = 
Here is the menu:
1.Classic Panipuri:10
2.Spicy Panipuri:15
3.Sweet Panipuri: ₹25
4. Bhel Puri: ₹30
5. Dahi Puri: ₹35
6. Chat Masala: ₹10
7. Special Combo (Panipuri + Bhel Puri): ₹50

print(menu)

choice = input("Enter the number of your chosen item: ")

if choice == '1':
    print("You've chosen Classic Panipuri! That's ₹10.")
if choice == '2':
    print("You've chosen Spicy Panipuri! That's ₹10.")
elif choice == '3':
    print("You've chosen Sweet Panipuri! That's ₹25.")
elif choice == '4':
    print("You've chosen Bhel Puri! That's ₹30.")
elif choice == '5':
    print("You've chosen Dahi Puri! That's ₹35.")
elif choice == '6':
    print("You've chosen Chat Masala! That's ₹10.")
elif choice == '7':
    print("You've chosen the Special Combo! That's ₹50.")
elif choice=='' and '':
    print("you have chosen", ('' + ''))
else:
    print("Invalid choice. Please try again.")'''


print("Welcome to Ammu's Panipuri Center!")

menu = {
    "1": {"name": "Classic Panipuri", "price": 10},
    "2": {"name": "Spicy Panipuri", "price": 15},
    "3": {"name": "Sweet Panipuri", "price": 25},
    "4": {"name": "Bhel Puri", "price": 30},
    "5": {"name": "Dahi Puri", "price": 35},
    "6": {"name": "Chat Masala", "price": 10},
    "7": {"name": "Special Combo (Panipuri + Bhel Puri)", "price": 50}
}

print("\n--- Menu ---")
for key, value in menu.items():
    print(f"{key}. {value['name']}: ₹{value['price']}")

choice = input("\nEnter the number of your chosen item: ")

if choice in menu:
    print(f"\nYou've chosen {menu[choice]['name']}! That's ₹{menu[choice]['price']}.")
elif choice in menu:
    print(f"\nYou've chosen {menu[choice][name]and menu[choice]['name']}! That's ₹{menu[choice]['price']}.")
else:
    print("Invalid choice. Please try again.")



    


