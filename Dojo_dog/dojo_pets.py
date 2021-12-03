from classes.pets import Dog, Chihuahua
from classes.ninja import Ninja


ninja1 = Ninja("Francis", "James", "biscuts", "Science Diet", Chihuahua("Goose", {"sit", "lay down"}, 75, 75, "bark"))
ninja2 = Ninja("Francis", "James", "biscuts", "Science Diet", Chihuahua("Jolly", {"sit", "lay down"}, 75, 75, 'bark'))

print(ninja1.pet)

ninja1.bathe(ninja1.pet)
ninja1.walk(ninja1.pet)
print(ninja1.pet.health)
ninja1.feed(ninja1.pet)
print(ninja1.pet.health)
