from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        #require implementing classes to provide a shipping calculation
        pass