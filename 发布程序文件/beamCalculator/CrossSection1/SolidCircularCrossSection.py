import sys
sys.path.append("../Beam")
sys.path.append("")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("../Support")
from HollowCircularCrossSection import HollowCircularCrossSection
import math as maths


class SolidCircularCrossSection(HollowCircularCrossSection):

    def __init__(self,radius):
        super(SolidCircularCrossSection, self).__init__(radius, 0, "Solid Circular Cross-Section")

    def get_area_moment_of_inertia(self):
        Ix=(maths.pi * pow(self.outer_radius,4)) / 64
        print(Ix)
        return Ix
    def get_area_moment_of_inertiay(self):
        Iy=(maths.pi * pow(self.outer_radius,4)) / 64
        print('圆的惯性距y',Iy)
        return Iy
    def get_area_moment_of_inertiap(self):
        Ip=(maths.pi * pow(self.outer_radius,4)) / 32
        print('圆的惯性距p',Ip)
        return Ip
    def CWX(self):
        wx=(maths.pi * pow(self.outer_radius,3)) / 32
        print('圆的抗弯截面模量x',wx)
        return  wx
    def CWy(self):
        wy=(maths.pi * pow(self.outer_radius,3)) / 32
        print('圆的抗弯截面模量y', wy)
        return  wy
    def CWn(self):
        wn=(maths.pi * pow(self.outer_radius,3)) / 16
        print('圆的抗扭截面模量n', wn)
        return  wn


