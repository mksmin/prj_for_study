from switchables import Switchable
from switch_interface import SwitchBase


class PowerSwitch(SwitchBase):
    def __init__(self, client: Switchable):
        if not isinstance(client, Switchable):
            raise TypeError("Client should be switchable!")

        self.client = client
        self.on = False
        self.client.turn_off()

    def is_turned_on(self):
        return self.on

    def toggle(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
