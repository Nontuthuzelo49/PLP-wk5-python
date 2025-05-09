# Activity 2: Polymorphism Challenge! 🎭
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method 'move'")

class Dog(Animal):
    def move(self):
        return "Barks and Runs on four legs."

class Bird(Animal):
    def move(self):
        return "Fly in the sky."

class Dolphin(Animal):
    def move(self):
        return "Swim in the ocean."
    

# Creating objects of each class and demonstrating polymorphism
dog = Dog()
bird = Bird()
dolphin = Dolphin()

# Generic function that can handle any Animal type
def animals_move(animals):
    for animal in animals:
        print(animal.move())

# Testing polymorphism with a list of animals
animals = [dog, bird, dolphin]
animals_move(animals)