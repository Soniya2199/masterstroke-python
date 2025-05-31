class School:
    def __init__(self, name):
        self.name = name

class Student(School):
    def __init__(self, name, school_name, marks):
        super().__init__(school_name)
        self.student_name = name
        self.marks = marks 

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def display_details(self):
        print(f"Student Name: {self.student_name}")
        print(f"School Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average():.2f}")
        print(f"Grade: {self.get_grade()}")
        print("-" * 30)

students = [
    Student("Alice", "Greenwood High", [85, 90, 78, 92, 88]),
    Student("Bob", "Greenwood High", [76, 80, 72, 68, 74]),
    Student("Charlie", "Greenwood High", [95, 98, 97, 99, 100])
]

for student in students:
    student.display_details()