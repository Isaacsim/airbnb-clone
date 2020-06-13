class Dog:
    def __init__(self):
        print("woor")

    def pee(self):
        print("illpee")


class Puppy(Dog):
    def __init__(self):
        print("im tiny")
        super().__init__()

    def pee(self):
        print("go to the park")
        super().pee()


p = Puppy()

p.pee()
