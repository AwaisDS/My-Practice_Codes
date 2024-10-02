# # num1=int(input("enter first number:"))
# # num2=int(input("enter second number:"))

# # sum=num1+num2

# # print(f"Sum is {sum}")

# # a=float(input("enter first number"))
# # b=float(input("enter second number"))
# # average=(a+b)/2

# # print(f"Averageis {average}")

# #Calculator program

# print("__________Calculator__________")
# num1=int(input("enter first number :"))
# num2=int(input("enter second number :"))

# oper=input("Choose a operator \n+\n-\n/\n*\n")

# if oper == "+":
#     res=num1+num2
#     print(f"Sum is {res}")
# if oper == "-":
#     res=num1-num2
#     print(f"Subtraction is {res}")   
# if oper == "/":
#     res=num1/num2
#     print(f"Divide is {res}")
# if oper == "*":
#     res=num1*num2
#     print(f"Multiplication is {res}")



# name=input("enter student name :")
# marks=int(input(f"enter marks of {name} :"))

# if(marks >= 90):
#     grade="A"
# elif(marks >= 80 and marks < 90):
#     grade="B"
# elif(marks >= 70 and marks < 80):
#     grade="C"
# elif(marks >= 60 and marks < 70):
#     grade="D"
# elif(marks >= 50 and marks < 60):
#     grade="E"
# else:
#     grade="F"

# print(f"Grade of {name} is {grade} with marks {marks}")

#to print a number is even or odd
# num=int(input("enter number :"))
# rem=num % 2

# if(rem==0):
#     print("number is even")
# else:
#     print("number is odd")


#To find th largest number

# a=int(input("Enter First number:"))
# b=int(input("Enter Second number:"))
# c=int(input("Enter Third number:")) 

# if(a > b and a > c):
#     print(f"{a} is the Largest number")
# elif(b > a and b > c):
#     print(f"{b} is the Largest number")
# else:
#     print(f"{c} is the Largest number")

#to check if a number is multiple of 7(or some other number)

# num=int(input("Enter number :"))
# multiple=int(input("Enter multiple number :"))
# rem=num % multiple

# if(rem==0):
#     print(f"Yes! it is devisible by {multiple} ...")
# else:
#     print(f"No! it is not devisible by {multiple} ...")


# def add(num1,num2):
#     res=num1+num2
#     print(res)
#     return res
# def sub(num1,num2):
#     res=num1-num2
#     print(res)
#     return res
# def multiply(num1,num2):
#     res=num1*num2
#     print(res)
#     return res
# def devide(num1,num2):
#     if num2==0:
#         print("Can't devide by zero")
#         return
#     elif num2!=0:
#         res=num1/num2
#         print(res)
#         return res

# number1=int(input("Enter First number:"))
# number2=int(input("Enter second number:"))

# choice=int(input("Select operator:\n1.Add\n2.Sub\n3.Multiply\n4.Devide\n"))

# if choice==1:
#     add(number1,number2)
# elif choice==2:
#     sub(number1,number2)
# elif choice==3:
#     multiply(number1,number2)
# elif choice==4:
#     devide(number1,number2)
# else:
#     print("invalid selection.....")

