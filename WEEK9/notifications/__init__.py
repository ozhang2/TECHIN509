# Abstractions (Abstract Base Class)
from abc import ABC, abstractmethod

class NotificationMethod(ABC):
    @abstractmethod
    def send(seld, message):
        pass
