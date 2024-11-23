import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("")
from Support import Support


class RollerSupport(Support):

    def __init__(self, location, vertical_reaction=None):
        Support.__init__(self, location, "roller", vertical_reaction)
