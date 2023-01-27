import utils
import person


class Player(person.Person):
    def __init__(self) -> None:
        person.Person.__init__(self)
        self.id = 1
        self.currentAction: utils.Action = utils.Action.HIT
        self.splitCount = 0
