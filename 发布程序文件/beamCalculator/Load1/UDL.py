import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("")
sys.path.append("../Material")
sys.path.append("../Support")
from Load import Load


class UDL(Load):

    def __init__(self, magnitude, start_location, end_location, order = 0):
        super(UDL, self).__init__(magnitude, start_location, end_location)
        self.order = order