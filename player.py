from person import Person

class Player(Person):
    def __init__(self) -> None:
        Person.__init__(self)
        self.id = 1
        self.hello()

    def hello(self):
        print("hello from player")