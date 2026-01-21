from abc import ABC, abstractmethod


class Parkable(ABC):
    @abstractmethod
    def park(self, parking):
        pass

    @abstractmethod
    def unpark(self, parking):
        pass