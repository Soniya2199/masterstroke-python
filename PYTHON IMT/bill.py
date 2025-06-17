import datetime

# Load grocery items from a file
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

# Display available items
def display_items(items):
    print("\nAvailable Items:")
    for item, price in items.items():
        print(f"{item.title()} - ₹{price}/unit")

# Add item to the cart
def add_to_cart(items, cart):
    item = input("Enter item name: ").lower()
    if item in items:
        try:
            qty = int(input("Enter quantity: "))
            cart[item] = cart.get(item, 0) + qty
            print(f"{qty} x {item.title()} added.")
        except ValueError:
            print("Invalid quantity.")
    else:
        print("Item not available.")

# Generate unique bill number
def generate_bill_number():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Generate and save bill to a text file
def generate_bill(items, cart, customer_name, phone):
    bill_no = generate_bill_number()
    total = 0
    lines = []

    lines.append("===== GROCERY BILL =====")
    lines.append(f"Bill No   : {bill_no}")
    lines.append(f"Customer  : {customer_name}")
    lines.append(f"Phone     : {phone}")
    lines.append("------------------------")

    for item, qty in cart.items():
        price = items[item]
        cost = qty * price
        total += cost
        lines.append(f"{item.title():10} x {qty:<3} = ₹{cost}")

    lines.append("------------------------")
    lines.append(f"Total Amount : ₹{total}")
    lines.append("========================")

    # Print bill
    print("\n".join(lines))

    # Save to text file
    filename = f"bill_{bill_no}.txt"
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"\nBill saved as '{filename}'")


def main():
    items = load_items("items.txt")
    if not items:
        return

    cart = {}

    while True:
        print("\n1. Show Items\n2. Add to Cart\n3. Generate Bill\n4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            display_items(items)
        elif choice == "2":
            add_to_cart(items, cart)
        elif choice == "3":
            if not cart:
                print("Cart is empty!")
                continue
            name = input("Customer Name: ")
            phone = input("Phone Number : ")
            generate_bill(items, cart, name, phone)
            cart.clear()
        elif choice == "4":
            print("Thanks for visiting!")
            break
        else:
            print("Invalid option.")

if __name__=='__main__':
    main()

