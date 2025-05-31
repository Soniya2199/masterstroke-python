class Phone:
    charger='C-Type' #! class variable
    def __init__(p,brand,price):
        p.brand=brand #! instance variable 
        p.price=price
    def display(p):
        print('Brand:',p.brand)
        print('Price:',p.price)
        print('Charger:',p.charger)
mi=Phone('Redmi',13000)
mi.display()

