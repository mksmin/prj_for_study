from abc import ABC, abstractmethod


class SwitchBase(ABC):

    @abstractmethod
    def toggle(self):
        pass

    @abstractmethod
    def is_turned_on(self):
        pass

    def is_turned_off(self):
        return not self.is_turned_on()

    @property
    def turned_on(self):
        return self.is_turned_on()

    @property
    def turned_off(self):
        return not self.turned_on
