import random as r
import datetime as dt
import re


class Invoice:

    def __init__(self):
        self.customer_name = input("Enter the Name:")
        self.customer_mobileno = self.validate_phno()
        self.otp_generation()
        self.bill_no = self.generate_bill_number()
        self.items = []
        self.product()
        self.generate_invoice()

    def otp_generation():
        generate_otp = r.randint(1000, 9999)
        print("One Time code:", generate_otp)
        otp = int(input("Enter your otp:"))
        if otp == generate_otp:
            print("Verification Successful")
        else:
            print("Invalid code")

    def validate_phno(customer_mobileno):
        customer_mobileno = input("Enter the Mobile Number:")
        pattern = re.compile(r"^[6-9]\d{9}$")
        return pattern.match(customer_mobileno)

    def generate_bill_number():
        return dt.datetime.now().strftime("%Y%m%d%H%M%S")

    bill_no = generate_bill_number()

    items = []

    def product(items):

        while True:
            product_name = input("Enter the Product:").capitalize()
            if product_name.lower() == "done":
                break
            qty = int(input("Enter the Quantity:"))
            pro_per_price = float(input("Enter the Price:"))
            total_price = qty * pro_per_price
            items.append((product_name, qty, pro_per_price, total_price))
     
    while True:
        validate_phno(customer_mobileno)
        if validate_phno(customer_mobileno):
            otp_generation()
            break
        else:
            print("Invalid Number")
            customer_mobileno = input("Enter the Mobile Number:")

    product(items)

    def generate_invoice(self):
        total_amount = 0
        head = "INVOICE"
        print("Customer Name =", customer_name)
        print("Mobile Number =", customer_mobileno)
        print("Invoice no =", bill_no)
        print()
        print(head.center(50))
        print("=" * 46)
        print("ProductName\tQuantity\tPrice\tTotal")
        print()

        for item in items:
            product_name, qty, pro_per_price, total_price = item
            print(product_name, "\t\t", qty, "\t\t", pro_per_price, "\t", total_price)
            total_amount += total_price

        print("=" * 46)
        head = f"Total Amount:{total_amount}"
        print(head.rjust(45))
        print("\nThanks for visiting!")


i = Invoice()
