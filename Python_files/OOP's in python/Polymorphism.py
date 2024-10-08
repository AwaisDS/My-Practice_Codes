class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Function to demonstrate polymorphism
def animal_speak(animal):
    return animal.speak()

# Creating instances of different animals
dog = Dog()
cat = Cat()
bird = Bird()

# Calling the speak method for each animal
print(animal_speak(dog))  # Output: Woof!
print(animal_speak(cat))  # Output: Meow!
print(animal_speak(bird)) # Output: Tweet!
