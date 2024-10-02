# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print("Even numbers:", even_numbers)

# fav_movies=[]
# movie1=input("Enter first movie name :")
# movie2=input("Enter second movie name :")
# movie3=input("Enter third movie name :")

# fav_movies.append(movie1)
# fav_movies.append(movie2)
# fav_movies.append(movie3)

# print(f"movies are {fav_movies}")


#------------Dictionary-------------#


# info={
#     "name":"Ahmed Awais",
#     "age":20,
#     "gender":"male",
#     "topics":("dict","sets")
# }

# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("name"))
# print(info.update({"city":"karachi"}))
# print(info)

#-----Nested dictionary

# student={
#     "name":"Ahmed Awais",
#     "age":20,
#     "gender":"male",
#     "subject":{
#         "programming":89,
#         "comp":78,
#         "chem":76
#     },
#      "topics":("dict","sets")
# }

# print(student)


#------------sets-------------#

# set1={1,2,3,4,5}

# print(set1)
# print(type(set1))

# emptyset=set() #empty set
# emptyset.add(4)
# emptyset.add(5)
# emptyset.add(8)

# emptyset.remove(5)
# emptyset.pop()
# print(emptyset)

# set1={1,8,3}
# set2={4,8,6}
# print(set1.intersection(set2))
# print(set1.union(set2))

#-------------Loops--------------------

#________While Loops
# count=10
# while count >= 1:
#     print(count - 1)
#     count -=1
# print(count)

# count=1
# while count <= 100:
#     print(count)
#     count +=1

# i=100
# while i >= 1:
#     print(i)
#     i -=1

# n=int(input("Enter table : "))
# print(" ")
# i=1

# while i<=10:
#     print(f"{n} X {i} = {i*n}")
#     i +=1

# list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i=0
# len=len(list)
# while i<len:
#     print(list[i])
#     i+=1

#----------Continue statement

# nums=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# i=0
# x=49
# len=len(nums)
# while i<len:
#     if (nums[i] == x):
#         i += 1
#         continue
#     print(nums[i])
#     i+=1

#---------------break statement

# nums=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# i=0
# x=49
# len=len(nums)
# while i<len:
#     if (nums[i] == x):
#         break
#     print(nums[i])
#     i+=1

#_________For Loops

# num=(1,2,3,4,5,6)

# for val in num:
#     print(val)

# str="Awais"
# for i in str:
#     if(i == 'a'):
#         continue
#     print(i)
# else:
#     print("End of for loop")

# str="Awais"
# for i in str:
#     if(i == 'a'):
#         print(f"Found {i}")
#         break
#     else:
#         print("Finding......")
#   #  print(i)
# else:
#     print("End of for loop")

# list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# x=36
# for i  in list:
#     if(i==x):
#         print(f"Found {x}")
#         break
#     else:
#         print("Finding....")

# for i in range(3):
#     print("hi")

#------------Functions

# def sum(a,b):
#     return a+b

# print(sum(5,8))
# print(sum(5,2))

# def average(a,b,c):
#     av=(a+b+c)/3
#     return av

# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))

# output=average(num1,num2,num3)

# print(f"average is equal to : {output}")

# def c(n=4,b=6):
#     print(n*b)
#     return n*b
# c()

# cities=["karachi","hydrabad","lahore","islamabad","gujrat"]
# heros=["superman","ironman","thor"]

# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(cities)


# def cal_fact(n):
#     fact=1
#     for i in range (1,n+1):
#         fact *=i
#     print(fact)
# cal_fact(5)

# def currency_change(a,b):
#     change=a*b
#     return change

# amount=int(input("Enter amount in usd : "))
# rate=int(input("Enter usd price in ur country : "))

# print(currency_change(amount,rate))

# def check(n):
#     if n%2==0:
#         print("Even")
#     elif n%2==1:
#         print("Odd")
# num=int(input('Enter number :'))
# check(num)

#Recursive function

# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
# show(7)

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return factorial(n-1)*n

# print(factorial(5))

# def sum(n):
#     if n==0:
#         return 0
#     return sum(n-1)+n
# print(sum(4))

# def print_list(list,idx=0):
#     if (idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# languages=['python','R','java','c++']
# print_list(languages)
