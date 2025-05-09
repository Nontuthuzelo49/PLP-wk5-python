# PLP-wk5-python
### **Python OOP Assignment**

## 📌 **Project Overview**
This project focuses on:
- **Creating a class** to represent a superhero with attributes and methods.
- **Implementing inheritance** for extending functionality.
- **Exploring polymorphism** by defining a common `move()` method in different classes.

---

## 🦸‍♂️ **Assignment 1: Superhero Class**
A Python class representing a **Superhero** with:
- **Attributes**: Name, powers, weakness.
- **Methods**: Reveal powers, weaknesses, and use a specific power.
- **Inheritance**: `RegularHero` extends `Superhero` and adds a secret identity.

### ✅ **Example Code:**
```python
class Superhero:
    def __init__(self, name, powers, weakness):
        self.name = name
        self.powers = powers
        self.weakness = weakness

    def show_powers(self):
        print(f"{self.name} has the following powers: {self.powers}")

    def reveal_weakness(self):
        print(f"{self.name}'s weakness is {self.weakness}.")

    def use_power(self, power):
        if power in self.powers:
            print(f"{self.name} uses {power}!")
        else:
            print(f"{self.name} doesn't have the power {power}.")

# Inheritance Layer
class RegularHero(Superhero):
    def __init__(self, name, powers, weakness, secret_identity):
        super().__init__(name, powers, weakness)
        self.secret_identity = secret_identity

    def reveal_secret(self):
        print(f"{self.name}'s secret identity is {self.secret_identity}.")
```

---

## 🎭 **Activity 2: Polymorphism Challenge**
A set of **animal classes** implementing the `move()` method differently:
- **Dog → "Barks and Runs on four legs."**
- **Bird → "Flies in the sky."**
- **Dolphin → "Swims in the ocean."**

### ✅ **Example Code:**
```python
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method 'move'")

class Dog(Animal):
    def move(self):
        return "Barks and Runs on four legs."

class Bird(Animal):
    def move(self):
        return "Flies in the sky."

class Dolphin(Animal):
    def move(self):
        return "Swims in the ocean."

# Testing polymorphism
animals = [Dog(), Bird(), Dolphin()]
for animal in animals:
    print(animal.move())
```

---

## 🚀 **How to Run**
1️⃣ Ensure **Python** is installed.  
2️⃣ Copy the provided code into a Python file (`oop_project.py`).  
3️⃣ Run the script using:
```sh
python oop_project.py
```
4️⃣ Observe **encapsulation, inheritance, and polymorphism in action**.

---
