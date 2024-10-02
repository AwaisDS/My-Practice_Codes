# #print report card of a student

# name=input("Enter your name:")
# school=input("Enter you school:")
# n=int(input("enter number of courses:"))

# totalmarks=int(input("enter total marks"))
# obtainedmarks=0

# for i in range (n):
#     course=input("course name : ")
#     marks=int(input(f"enter marks for {course} : "))
#     obtainedmarks+= marks
# percentage=0
# status="Pass"
# percentage=int((obtainedmarks/totalmarks * 100))

# if(percentage >= 85 and percentage < 100):
#     grade="A1"
# if(percentage >= 75 and percentage < 85):
#     grade="A"
# if(percentage >= 65 and percentage < 75):
#     grade="B"
# if(percentage >= 55 and percentage < 65):
#     grade="C"
# if(percentage >= 45 and percentage < 55):
#     grade="D"
# if(percentage < 45):
#     grade="F"
#     status="Fail"

# print("\n\n--------------------------------------------")
# print(f"Name : {name}\t\tCollege : {school}")
# print(f"Total Marks : {totalmarks} \nObtained Marks : {obtainedmarks}")
# print(f"Percentage : {percentage} % \nGrade : {grade} \nStatus : {status}")
# print("--------------------------------------------")

# #WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

# list=["m","a","a","m"]
# list=[]
# n=int(input("How many letters are in your word.."))
# for i  in range(n):
#     list.append(input(f"Enter character {i + 1} :"))
# copied=list.copy()
# copied.reverse()
# print(list)
# if(list==copied):
#     print("\nThis is palindrome")
# else:
#     print("this is not palindrome")

# #WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# fav_movies=[]
# movie1=input("Enter first movie name :")
# movie2=input("Enter second movie name :")
# movie3=input("Enter third movie name :")

# fav_movies.append(movie1)
# fav_movies.append(movie2)
# fav_movies.append(movie3)

# print(f"movies are {fav_movies}")

# #WAP to count the number of students with the “A” grade in the following tuple

# grades=("A","D","F","A","A","C")
# print(grades.count("A"))

# #Store the above values in a list & sort them from “A” to “D”

# grades=["A","D","F","A","A","C"]
# grades.sort()
# print(grades)

# #Let's say you want to filter a list of numbers and create a new list containing only the 
# #even numbers from the original list.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print("Even numbers:", even_numbers)


#Store following word meanings in a python dictionary :
#table : “a piece of furniture”,“list of facts & figures” , cat : “a small animal”

# wordmeaning={
#     "table":{
#         "meaning1":"a piece of furniture",
#         "meaning2":"list of facts & figures"
#     },
#     "cat":"a small animal"
# }

# print(wordmeaning)

#You are given a list of subjects for students. Assume one classroom is required for 1
#subject. How many classrooms are needed by all students.
#”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C

# classrooms={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
#     }
# rooms=len(classrooms)

# print(f"total classrooms for classes of this subjects are {rooms} .")

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value

# student={}

# for i in range(3):
#     sub=input("Enter sunject")
#     marks=int(input(f"Enter {sub} marks:"))
#     student.update({sub:marks})

# With out loop------

# phym=int(input("Enter phy marks:"))
# student.update({"phy":phym})

# mathm=int(input("Enter math marks:"))
# student.update({"math":mathm})

# compm=int(input("Enter comp marks:"))
# student.update({"comp":compm})
# print(student)



#-----------

# num=[]
# even_sum=0
# ele=int(input("enter length of numbers in this list :"))

# for i in range(ele):
#     numbers=int(input("Enter number :"))
#     num.append(numbers)
#     if numbers%2==0:
#         even_sum+=numbers
# print(num)
# print(even_sum)

#-----------

# import string

# def count_word_frequency(sentence):
#     # Remove punctuation and convert the sentence to lowercase
#     sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
#     # Split the sentence into words
#     words = sentence.split()
    
#     # Create a dictionary to store word frequencies
#     word_frequency = {}
    
#     # Count the frequency of each word
#     for word in words:
#         if word in word_frequency:
#             word_frequency[word] += 1
#         else:
#             word_frequency[word] = 1
    
#     return word_frequency

# def main():
#     # Prompt the user to enter a sentence
#     sentence = input("Enter a sentence: ")
    
#     # Count word frequency
#     word_frequency = count_word_frequency(sentence)
    
#     # Display word frequency
#     print("Word Frequency:")
#     for word, frequency in word_frequency.items():
#         print(f"{word}: {frequency}")

# if __name__ == "__main__":
#     main()
