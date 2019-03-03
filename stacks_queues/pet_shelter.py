"""
Problem:

Design a data structure for a pet shelter. The pet shelter must be able to add
a dog or add a cat and associate a timestamp with each new pet (you can use an
auto-increment id).

The data structure must also support removeDog and removeCat, which remove the
dog which has been here the longest (i.e. dequeue). The third operation to
support is removeAny, which removes either the oldest dog or oldest cat. Throw
an IndexError on any attempt to remove a pet from an empty shelter. Throw a
ValeError if inserting a dog in addCat or a cat in addDog.

Lastly, support numDogs(), numPets() and numCats(), which return the count for
dogs, pets or cats stored within the shelter.

Hints:

You can use isinstance to determine if an object is an instance of some base
class.
"""


from collections import deque

class Animal:

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "<Dog: {}>".format(name)

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "<Cat: {}>".format(name)

class PetShelter:

    def __init__(self):
        self._cats = deque()
        self._dogs = deque()
        self._id = 0

    def addDog(self, dog):
        if isinstance(dog, Dog):
            self._dogs.append((dog, self._id))
            self._id += 1
        else:
            raise ValueError('Require instance of Dog')

    def addCat(self, cat):
        if isinstance(cat, Cat):
            self._cats.append((cat, self._id))
            self._id += 1
        else:
            raise ValueError('Require instance of Cat')

    def removeDog(self):
        if not self._dogs:
            raise IndexError('No dog in the shelter')

        return self._dogs.popleft()

    def removeCat(self):
        if not self._cats:
            raise IndexError('No cats in the shelter')

        return self._cats.popleft()

    def removeAny(self):
        if not (self._cats or self._dogs):
            raise IndexError('No pets in the shelter')

        if self._dogs and (not self._cats):
            return self._dogs.popleft()

        if self._cats and (not self._dogs):
            return self._cats.popleft()

        cat1 = self._cats[0]
        dog1 = self._dogs[0]

        if cat1[1] < dog1[1]:
            return self._cats.popleft()
        else:
            return self._dogs.popleft()

    def numCats(self):
        return len(self._cats)

    def numDogs(self):
        return len(self._dogs)

    def numPets(self):
        return len(self._cats) + len(self._dogs)

if __name__ == "__main__":
    shelter = PetShelter()
    d1 = Dog("udon")
    c1 = Cat("meow")
    d2 = Dog("woof")
    d3 = Dog("pudding")
    c2 = Cat("cookie")
    c3 = Cat("binggan")
    shelter.addDog(d1)
    shelter.addCat(c1)
    shelter.addDog(d2)
    shelter.addDog(d3)
    shelter.addCat(c2)
    shelter.addCat(c3)
    print(shelter.numCats())
    print(shelter.numDogs())
    print(shelter.numPets())
    print(shelter.removeCat())
    print(shelter.removeDog())
    print(shelter.removeAny())
