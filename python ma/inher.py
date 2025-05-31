# # Parent class
# class Person:
#     def __init__(self, name, age):
#         self.name = name  # Instance variable for name
#         self.age = age    # Instance variable for age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Child class (inherits from Person)
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         # Call the constructor of the parent class
#         super().__init__(name, age)
#         self.student_id = student_id  # New attribute for Student

#     def display_student(self):
#         # Call parent class display method
#         self.display()
#         print(f"Student ID: {self.student_id}")

# # Creating an object of the Student class
# student1 = Student("Alice", 20, "S12345")

# # Displaying student details
# student1.display_student()


class A:
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

# Class C inherits from both A and B
class C(A, B):
    def method_C(self):
        print("Method C")

obj = C()
obj.method_A()  # Inherited from A
obj.method_B()  # Inherited from B
obj.method_C() 