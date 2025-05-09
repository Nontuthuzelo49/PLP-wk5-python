# Assignment 1: Design Your Own Class - Superhero 🦸‍♂️
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

# Inheritance Layer - RegularHero inherits from Superhero but might have different attribute handling
class RegularHero(Superhero):
    def __init__(self, name, powers, weakness, secret_identity):
        super().__init__(name, powers, weakness)
        self.secret_identity = secret_identity

    def reveal_secret(self):
        print(f"{self.name}'s secret identity is {self.secret_identity}.")
# Example of creating a Superhero object
superhero = Superhero("Superman", ["Flight", "Super Strength"], "Kryptonite")
superhero.show_powers()
superhero.reveal_weakness()
superhero.use_power("Flight")
