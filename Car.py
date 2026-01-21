from Parkable import Parkable
from Vehicle import Vehicle


class Car(Vehicle, Parkable):
    def __init__(self, registration: str):
        super().__init__(registration)

    def park(self, parking):
        print("Je me gare")

    def unpark(self, parking):
        print("Je me dégare")
