import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("")
sys.path.append("../Support")
from Material import Material


class CastIronGrade20(Material):
    DENSITY = 7850#kg/mm^3
    TENSILE_MODULUS = 210000#mpa
    TENSILE_STRENGTH = 140#mpa

    def __init__(self):
        super(CastIronGrade20, self).__init__("Steel", CastIronGrade20.DENSITY, CastIronGrade20.TENSILE_MODULUS, CastIronGrade20.TENSILE_STRENGTH)