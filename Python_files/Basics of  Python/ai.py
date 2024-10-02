intro='hi this is awais i am learning data science now and i am on a path of data camp associate data scientist certificate'

def question():
    print('1.what is your name ?')
    print('2.Introduce yourself ?')
    print('3.what skills you have ?')

    choice=int(input('Enter your choice...'))

    if choice == 1:
        print('My name is awais')
    elif choice == 2 :
        print(intro)
    elif choice == 3:
        print('PYTHON  JAVA  C#  C ')
    else :
        print('Invalid choice')

question()