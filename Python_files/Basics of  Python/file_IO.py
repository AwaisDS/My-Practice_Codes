# file=open("awais.txt","r")
# data=file.read()
# print(data)
# file.close()

# f=open("awais.txt","w")
# data=f.write("Hello World !")
# f.close()
# f=open("awais.txt","r")
# data1=f.read()
# print(data1)
# f.close()

# f=open("awais.txt","w")
# f.write("awais")
# f.close()

# f=open("awais.txt","a")
# f.write("\nAli")
# f.close()

# with  open ("awais.txt", "r") as f:
#     data=f.read()
#     print(data)

# import os
# os.remove("")

# with  open('awais.txt', 'r') as f:
#     data=f.read()
#     print(data)

# with    open ('awais.txt','w')   as f:
#     f.write("hi everyone\nwe are learning file i/o \nusing java\ni like java")

# with     open ('awais.txt','r')   as f:
#     data=f.read()
# new_data=data.replace("java","python")
# print(new_data)

# with open('awais.txt','w')as f:
#     f.write(new_data)

# def check_for_word(word):
#     with  open('awais.txt','r') as f:
#         data=f.read()
#     word=data.find(word)

#     if  word!=-1:
#         print("The word is present at position ",word)
#     else:
#         print("The word is not present in the text.")

# check_for_word("using")

# def check_for_line(word):
#     word=word
#     line_no=1
#     data=True
#     with  open('awais.txt','r') as  f:
#         while data:
#             data=f.readline()
#             if (word in data):
#                 print(f"{word} found on line {line_no}")
#                 return
#             line_no+=1
#     return -1
            
# check_for_line("using")
# check_for_line("are")
# check_for_line("python")
# check_for_line("by")


# count=0
# with   open ('awais.txt', 'r' ) as file :
#     data=file.read()
#     nums=data.split(",")
#     for i in nums:
#         if(int(i)%2==0):
#             count+=1
# print(count)