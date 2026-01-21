from abc import ABC


class Vehicle(ABC):
    __registration: str

    def __init__(self, registration: str):
        self.__registration = registration

    @property
    def Registration(self) -> str:
        return self.__registration

