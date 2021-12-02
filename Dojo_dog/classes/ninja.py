class Ninja:
    def __init__(self, first_name, last_name , treats , pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.food = pet_food
        self.pet = pet

    def walk(self, pet):
        self.pet.play()

    def feed(self, pet):
        self.pet.eat()

    def bathe(self, pet):
        self.pet.noise()