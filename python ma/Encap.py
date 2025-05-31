class MyClass:
    def __init__(self, public_data, _protected_data, __private_data):
        self.public_data = public_data  # Public
        self._protected_data = _protected_data  # Protected
        self.__private_data = __private_data  # Private

    def public_method(self):
        print(f"Public method: {self.public_data}")

    def _protected_method(self):
        print(f"Protected method: {self._protected_data}")

    def __private_method(self):
        print(f"Private method: {self.__private_data}")

c=MyClass('a','b','c')
print(c.public_data)
# print(c.__private_data) #! cannot be accessed
print(c._protected_data) #! accessed only within class 

c.public_method() 
# c.__private_method()
c._protected_method()