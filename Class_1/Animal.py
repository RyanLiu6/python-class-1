class Info:
    type = ""
    height = -1
    weight = -1
    age = -1


class Animal:
    # Base Class

    def __init__(self, name, info):
        self.name = name
        self.type = info.type
        self.height = info.height
        self.weight = info.weight
        self.age = info.age
        self.friends = {}

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def getType(self):
        return self.type

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getAge(self):
        return self.age

    def doAction(self):
        print(self.species + " has no action")
        print("Please remind developer to implement action for " + self.species)
