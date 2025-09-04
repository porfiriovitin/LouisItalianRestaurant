from abc import ABC, abstractmethod

class GetTableNumbersInterface(ABC):

    @abstractmethod
    def GetTableNumbers(self) -> list:
        pass