from Car import Car
from MotorBike import MotorBike
from Parking import Parking
from Tank import Tank

myParking = Parking()
twingo = Car("15rt99")
titine = MotorBike("89jk45")
grosTruc = Tank("Leclerc01")

myParking.addVehicle(twingo)
myParking.addVehicle(titine)
myParking.addVehicle(grosTruc)

