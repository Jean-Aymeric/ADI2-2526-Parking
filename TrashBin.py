from Parkable import Parkable


class TrashBin(Parkable):
    def __init__(self):
        ...

    def park(self, parking):
        print("Quelqu'un m'a déposé dans le parking")

    def unpark(self, parking):
        print("Quelqu'un est venu me remorquer depuis le parking")

