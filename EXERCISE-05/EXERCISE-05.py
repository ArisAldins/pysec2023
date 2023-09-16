class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Mani sauc {self.name} un mani ir {self.age} gadi")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} (Students ar ID: {self.student_id}) studē {subject}.")

# personas instance
person1 = Person("Berta", 88)

# studenta instance
student1 = Student("Miervaldis", 20, "KI-01")

# izmanto metodes no personas klases
person1.introduce()

# izmanto metodes no studenta klases
student1.introduce()
student1.study("PySec2023")

#Inheritance ļauj studenta klasei mantot īpašības un metodes no personas klases papildus pieliekot savas.
