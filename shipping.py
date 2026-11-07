from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        #require implementing classes to provide a shipping calculation
        pass