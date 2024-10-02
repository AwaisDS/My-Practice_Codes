# class Car:
#     @staticmethod
#     def start(name):
#         print(f"{name} is started..")
#     @staticmethod
#     def stop(name):
#         print(f"{name} is stopped..")

# class Toyotocar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(Toyotocar):
#     def  __init__(self,type,name):
#         self.type=type
#         self.name=name

# car1=Fortuner("electric","Fortuner")
# car1.start(car1.name)

#----Multiple inheritance

# class Mobile:
#     def Mobile_Welcome(self):
#         print("This is a Mobile")

# class Laptop:
#     def Laptop_welcome(self):
#         print("This is a laptop")

# class Website(Mobile,Laptop):
#     def welcome(self):
#         print("This is a Website")

# w1=Website()
# w1.Mobile_Welcome()
# w1.Laptop_welcome()
# w1.welcome()

#--Super keyword

# class Parent:
#     def __init__(self,age,gender):
#         self.age=age
#         self.gender=gender

# class Child(Parent):
#     def __init__(self,name,age,gender):
#         super().__init__(age,gender)
#         self.name=name

# c1=Child("Awais",44,"male")
# print(f"My name is {c1.name} and my father age  is {c1.age} gender is {c1.gender}")