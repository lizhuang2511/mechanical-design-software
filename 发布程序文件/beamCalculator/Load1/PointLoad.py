import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("")
sys.path.append("../Material")
sys.path.append("../Support")
from Load import Load


class PointLoad(Load):

    def __init__(self,magnitude,start_location):
        super(PointLoad, self).__init__(magnitude, start_location, start_location) #For point load start location = end location