class Student:
    college_name="Bahria College "
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
   
s1=Student("Ahmed Awais",20,"A")
s2=Student("Ali",21,"B")
s3=Student("Asad",22,"C")

def display():
    print(f"Student name is {s1.name} age {s1.age} and he scores {s1.grade} Grade study in {s1.college_name}")
    print(f"Student name is {s2.name} age {s2.age} and he scores {s2.grade} Grade study in {s2.college_name}")
    print(f"Student name is {s3.name} age {s3.age} and he scores {s3.grade} Grade study in {s3.college_name}")

display()