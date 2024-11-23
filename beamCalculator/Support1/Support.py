from abc import ABC
import sys
sys.path.append("../Calculator/Beam")
sys.path.append("../Calculator/CrossSection")
sys.path.append("../Calculator/Load")
sys.path.append("../Calculator/Material")
sys.path.append("../Calculator/Support")
from PointLoad import PointLoad


class Support(ABC):

    def __init__(self, location, supportType=None, vertical_reaction=None):
        self.location = location
        self.vertical_reaction = vertical_reaction
        self.supportType = supportType

    def set_vertical_reaction(self, magnitude):
        new_vertical_reaction = PointLoad(magnitude,self.location)
        self.vertical_reaction = new_vertical_reaction