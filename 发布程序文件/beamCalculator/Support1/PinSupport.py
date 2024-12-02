import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("")
from PointLoad import PointLoad
from Support import Support


class PinSupport(Support):

    def __init__(self, location, vertical_reaction=None, horizontal_reaction=None):
        Support.__init__(self, location, "pin", vertical_reaction)
        self.horizontal_reaction = horizontal_reaction

    def set_horizontal_reaction(self,magnitude):
        new_horizontal_reaction = PointLoad(magnitude, self.location)
        self.horizontal_reaction = new_horizontal_reaction