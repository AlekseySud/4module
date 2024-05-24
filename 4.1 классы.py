class Student:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def study(self):
        self.read()
        print(f"Посмотри! Ученик {self.name} учится!")

    def read(self):
        print("Какая интересная книга")
    def chill(self):
        print(f"Пойду-ка полежу, подумаю о своем любимом предмете - {self.subject}")



student = Student("Степа", "10", "математика")
print(f"Ученик идет: {student.name}, ему {student.age} лет, его любимый предмет - {student.subject}")
student.read()

second_student = Student("Егор", "15", "труд")
second_student.study()