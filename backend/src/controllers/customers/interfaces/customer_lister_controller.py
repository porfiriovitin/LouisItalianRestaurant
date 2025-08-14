from abc import ABC, abstractmethod

class CustomerListerControllerInterface(ABC):
    @abstractmethod
    def list(self)->dict:
       pass