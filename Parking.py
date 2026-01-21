from Parkable import Parkable


class Parking:
    __vehicles: []

    def __init__(self):
        self.__vehicles = []

    def addVehicle(self, vehicle: Parkable):
        if vehicle not in self.__vehicles:
            self.__vehicles.append(vehicle)
            vehicle.park(self)

    def removeVehicle(self, vehicle: Parkable):
        if vehicle in self.__vehicles:
            self.__vehicles.remove(vehicle)
            vehicle.unpark(self)