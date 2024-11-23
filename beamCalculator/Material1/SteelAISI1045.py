
from Material import Material


class SteelAISI1045(Material):
    DENSITY = 7850#密度
    TENSILE_MODULUS = 210000#拉伸模量
    TENSILE_STRENGTH = 585#抗拉强度
    qibianmoliang=TENSILE_MODULUS/2*(1+0.3)#增加这里
    def __init__(self):
        super(SteelAISI1045, self).__init__("Steel", SteelAISI1045.DENSITY, SteelAISI1045.TENSILE_MODULUS, SteelAISI1045.TENSILE_STRENGTH)