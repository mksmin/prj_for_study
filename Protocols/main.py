"""
Протоколы или интерфесы нужны чтобы объяснить какой объект хотим получить
В питоне на базовом уровне их нет, поэтому их нужно реализовывать через множественное наследование
"""

from switchables import Switchable, LightBulb, Radio
from power_switch import PowerSwitch


def main():
    print(Switchable)
    bulb = LightBulb()
    print(bulb)

    bulb.turn_on()
    bulb.turn_off()
    bulb.turn_on()

    switch = PowerSwitch(bulb)
    switch.toggle()
    switch.toggle()
    switch.toggle()
    switch.toggle()

    print("is turned on?", switch.is_turned_on())
    print("turned on?", switch.turned_on)
    print("is turned on?", switch.is_turned_off())
    print("turned on?", switch.turned_off)
    switch.toggle()
    print("is turned on?", switch.is_turned_on())
    print("turned on?", switch.turned_on)
    print("is turned on?", switch.is_turned_off())
    print("turned on?", switch.turned_off)

    print("===" * 3)

    radio = Radio()
    radio_switch = PowerSwitch(radio)
    radio_switch.toggle()
    radio_switch.toggle()
    radio_switch.toggle()
    print("radio switch turned on?", radio_switch.turned_on)
    print("radio switch turned off?", radio_switch.turned_off)
    radio_switch.toggle()
    print("radio switch turned on?", radio_switch.turned_on)
    print("radio switch turned off?", radio_switch.turned_off)

if __name__ == '__main__':
    main()
