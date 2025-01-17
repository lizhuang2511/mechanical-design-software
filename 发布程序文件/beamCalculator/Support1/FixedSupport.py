import sys
sys.path.append("../Load")
from Moment import Moment
from PointLoad import PointLoad
from Support import Support


class FixedSupport(Support):

    def __init__(self, location=0, vertical_reaction=None, horizontal_reaction=None, moment_reaction=None):
        Support.__init__(self, location, "fixed", vertical_reaction)
        self.horizontal_reaction = horizontal_reaction
        self.moment_reaction = moment_reaction

    def set_horizontal_reaction(self, magnitude):
        new_horizontal_reaction = PointLoad(magnitude, self.location)
        self.horizontal_reaction = new_horizontal_reaction

    def set_moment_reaction(self,magnitude):
        new_moment_reaction = Moment(magnitude, self.location)
        self.moment_reaction = new_moment_reaction