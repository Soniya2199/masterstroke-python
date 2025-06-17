import random as r

# otp=r.randint(1000,9999)
# user_name=input('Enter the name:')
# print('Here is the code:',otp)
# psw=int(input('Enter the otp:'))
# if psw==otp:
#     print('Verified successfully ')
# else:
#     psw!=otp
#     print('invalid code')


# def customer_Details():
#     generate_otp = r.randint(1000, 9999)
#     print("One Time code:", generate_otp)
#     otp = int(input("Enter your otp:"))
#     if otp == generate_otp:
#         print("Verification Successful")
#     else:
#         print("Invalid code")
# customer_name = input("Enter the Name:")
# customer_mobileno = input("Enter the Mobile Number:")
# customer_Details()

# a='hello'
# print(a.rjust(50))

def load_items(filename):
    items = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    name, price = line.strip().split(",")
                    items[name.lower()] = float(price)
    except FileNotFoundError:
        print("Error: 'items.txt' file not found.")
    return items

items=load_items("items.txt")

def display_items(items):
    print("\nAvailable Items:")
    for item, price in items.items():
        print(f"{item.title()} - ₹{price}/unit")

display_items(items)