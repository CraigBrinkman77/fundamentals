class Dog:
    def __init__(self, name, tricks, health, energy, noise):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise

    def play(self):
        self.health += 5

    def eat(self):
        self.health += 10
        self.energy += 5

    def sleep(self):
        self.health += 5
        self.energy += 5
    
    def make_noise(self):
        print(self.noise)

class Chihuahua ( Dog ):
    def __init__(self, name, tricks, health, energy, noise):
        super().__init__(name, tricks, health, energy, noise)