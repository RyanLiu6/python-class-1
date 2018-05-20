import Animal as am

class Dog(am.Animal):
    def __init__(self, name, info):
        super(Dog, self).__init__(name, info)
        self.species = "Canine"

    def doAction(self):
        print(self.name + " wags their tail.")


class Cat(am.Animal):
    def __init__(self, name, info):
        super(Cat, self).__init__(name, info)
        self.species = "Feline"
    pass

    def doAction(self):
        print(self.name + " lies on the ground and sleeps.")
