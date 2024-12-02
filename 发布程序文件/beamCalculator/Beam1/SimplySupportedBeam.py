from abc import ABC
import sys
sys.path.append("")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("../Support")
from Beam import Beam
from PinSupport import PinSupport
from RollerSupport import RollerSupport


class SimplySupportedBeam(Beam, ABC):

    def __init__(self, length, cross_section, material):
        Beam.__init__(self, length, cross_section, material)


    def add_support(self, type_of_support, location):
        if type_of_support.lower() == "pin":
            self.add_pin_support(location)

        elif type_of_support.lower() == "roller":
            self.add_roller_support(location)

    def add_pin_support(self, location):
        new_pin_support = PinSupport(location)
        self.supports.append(new_pin_support)

    def add_roller_support(self, location):
        new_roller_support = RollerSupport(location)
        self.supports.append(new_roller_support)



