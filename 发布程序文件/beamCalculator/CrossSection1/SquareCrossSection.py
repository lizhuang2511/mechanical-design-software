import sys
sys.path.append("../Beam")
sys.path.append("")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("../Support")
from RectangularCrossSection import RectangularCrossSection


class SquareCrossSection(RectangularCrossSection):
    
    def __init__(self, length):
        super(SquareCrossSection, self).__init__(length, length, "Square")

    # Override
    def get_area_moment_of_inertia(self):
        return pow(self.height, 4) / 12
