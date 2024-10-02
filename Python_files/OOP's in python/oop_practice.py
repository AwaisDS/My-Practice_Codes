#----create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print average

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def get_average(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print(f"hi {self.name} your average score is {sum/len(self.marks)}")

# s1=Student("Awais",[67,78,56])
# s1.get_average()
# #if you want to change the value of object attriute
# s1.name="Asad"
# s1.marks=[76,86,45]
# s1.get_average()

#----create a class that takes name and age as arguments in constructor.
#Then create a method to print name and age

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
    
#     def print_name_age(self):
#         print(f"hi {self.get_name()} your age is {self.get_age()}")

# p1=Person("Awais",20)
# p2=Person("sulemann",20)
# p1.print_name_age()
# p2.print_name_age()

#----Create Account class with 2 attributes - balance & account no.
#create methods for debit ,credit & print balance

# class Accounts:
   
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.account_no=account_no
#     def debit(self,amount):
#         self.balance-=amount
#         print(f"RS {amount} was debited from your account.")
#         print(f"Total amount is {self.balance}")    
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"RS {amount} was credited to your account.")
#         print(f"Total amount is {self.balance}")
#     def print_balance(self):
#         print(f"Total amount is {self.balance}")
# a1=Accounts(20000,12345)
# a1.credit(10000)

# while True:
#     choice=int(input("\nenter choice :\n1 to debit\n2 to credit\n3 to total amount "))
#     if choice==1:
#         deb_amount=int(input("enter amount to debit : "))
#         a1.debit(deb_amount)
#     elif choice==2:
#         cre_amount=int(input("enter amount to credit : "))
#         a1.credit(cre_amount)
#     elif choice==3:
#         a1.print_balance()
#     else:
#         print("invalid choice")

#     to_stop=int(input("\nDo you Want another Transaction\n1 to Yes\n2 to No\n"))
#     if to_stop==2:
#         break
#     else:
#         print("invalid choice")
    
# print("Thank you...")



# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return (22/7)*self.radius**2
#     def perimeter(self):
#         return 2*(22/7)*self.radius
    
# c1=Circle(10)
# print(c1.area())
# print(c1.perimeter())


# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.salary=salary
#         self.department=department

#     def print_details(self):
#         print(f"Role is {self.role}")
#         print(f"Salary is {self.salary}")
#         print(f"Department is {self.department}")
# e1=Employee("Manager","IT",100000)

# class Engineer(Employee):
#     def __init__(self,role,department,salary,name,age):
#         super().__init__(department,role,salary)
#         self.name=name
#         self.age=age

# E1=Engineer("Ai engineer","IT",100000,"Awais",22)
# E1.print_details()
# print(E1.name)
# print(E1.age)


# # Base class for University Personnel
# class UniversityPersonnel:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def display_info(self):
#         pass

# # Subclass for professors
# class Professor(UniversityPersonnel):
#     def __init__(self, name, id, department):
#         super().__init__(name, id)
#         self.department = department

#     def display_info(self):
#         print(f"Professor: {self.name}, Department: {self.department}")

# # Subclass for students
# class Student(UniversityPersonnel):
#     def __init__(self, name, id, major):
#         super().__init__(name, id)
#         self.major = major

#     def display_info(self):
#         print(f"Student: {self.name}, Major: {self.major}")

# # Subclass for administrative staff
# class AdminStaff(UniversityPersonnel):
#     def __init__(self, name, id, role):
#         super().__init__(name, id)
#         self.role = role

#     def display_info(self):
#         print(f"Admin Staff: {self.name}, Role: {self.role}")

# # Testing the system
# professor1 = Professor("Sir Faisal", "P001", "Computer Science")
# student1 = Student("Awais", "S001", "software")
# admin_staff1 = AdminStaff("Adnan", "A001", "HR")

# # Polymorphic behavior demonstration
# def display(info):
#     return info.display_info()

# display(professor1)
# display(student1)
# display(admin_staff1)

class Employee:
    def _init_(self, name, department, base_salary):
        self.name = name
        self.department = department
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary
    
    def _str_(self):
        return f"Employee Name: {self.name}, Department: {self.department}, Base Salary: {self.base_salary}"
    

class Manager(Employee):
    def _init_(self, name, department, base_salary, bonus):
        super()._init_(name, department, base_salary)
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus
    
    def _str_(self):
        return f"Manager Name: {self.name}, Department: {self.department}, Base Salary: {self.base_salary}, Bonus: {self.bonus}, Total Salary: {self.calculate_salary()}"
    

class Engineer(Employee):
    def _init_(self, name, department, base_salary, experience_years):
        super()._init_(name, department, base_salary)
        self.experience_years = experience_years
    
    def calculate_salary(self):
        return self.base_salary + (self.experience_years * 1000)
    
    def _str_(self):
        return f"Engineer Name: {self.name}, Department: {self.department}, Base Salary: {self.base_salary}, Experience Years: {self.experience_years}, Total Salary: {self.calculate_salary()}"
    

class Intern(Employee):
    def _init_(self, name, department, base_salary, months_duration):
        super()._init_(name, department, base_salary)
        self.months_duration = months_duration
    
    def calculate_salary(self):
        return self.base_salary / 2
    
    def _str_(self):
        return f"Intern Name: {self.name}, Department: {self.department}, Base Salary: {self.base_salary}, Months Duration: {self.months_duration}, Total Salary: {self.calculate_salary()}"



manager = Manager("Alice", "Management", 5000, 1000)
print(manager)

    # Create an Engineer instance
engineer = Engineer("Bob", "Engineering", 4000, 3)
print(engineer)

    # Create an Intern instance
intern = Intern("Charlie", "Research", 3000, 6)
print(intern)

