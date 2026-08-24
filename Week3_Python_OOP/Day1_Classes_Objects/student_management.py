class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}.")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_student_info(self):
        print(f"Student: {self.name}, Roll No: {self.roll_number}, Average Grade: {self.calculate_average():.2f}")

# Example usage
if __name__ == "__main__":
    s1 = Student("Aditya", 101)
    s1.add_grade(85)
    s1.add_grade(90)
    s1.display_student_info()
