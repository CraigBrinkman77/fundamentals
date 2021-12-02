class Dog:
    def __init__(self, name, tricks, health, energy):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def play(self):
        self.health += 5

    def eat(self):
        self.health += 10
        self.energy += 5

    def sleep(self):
        self.health += 5
        self.energy += 5

class Chihuahua ( Dog ):
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, tricks, health, energy)
    
    def noise(self):
        print("nooooo pweees")