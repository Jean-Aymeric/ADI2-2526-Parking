from Car import Car
from MotorBike import MotorBike
from Parking import Parking
from Tank import Tank
from TrashBin import TrashBin

myParking = Parking()
twingo = Car("15rt99")
titine = MotorBike("89jk45")
grosTruc = Tank("Leclerc01")
grosseBenne = TrashBin()

myParking.addVehicle(twingo)
myParking.addVehicle(titine)
myParking.addVehicle(grosseBenne)

