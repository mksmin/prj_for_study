from .switchable import Switchable


class Radio(Switchable):

    def turn_on(self):
        print("radio turned on")

    def turn_off(self):
        print("radio turned off")

