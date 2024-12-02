# -*- coding = utf-8 -*-
# @time:2023/4/17 10:47
# Author:lizhuang
# @File:应力计算.py
# @Software:PyCharm
import sys
import traceback
from abc import ABC, abstractmethod

# from BEAM.Load.Moment import Moment
# from BEAM.Load.PointLoad import PointLoad
# from BEAM.Load.UDL import UDL
import matplotlib.pyplot as plt
from sympy.physics.continuum_mechanics.beam import Beam as sympyBeam
from sympy import *
from sympy.abc import x
from symbeam import beam as symbeamBeam
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
import sys
sys.path.append("")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("../Support")
from PointLoad import PointLoad
from UDL import UDL
from Moment import Moment
from FixedSupport import FixedSupport
from PinSupport import PinSupport
from RollerSupport import RollerSupport
from 修改绘画 import sympyBeam_1
from SteelAISI1045 import SteelAISI1045
from Beam import  Beam,apply_support_fix
class beamstress(Beam):
    def __init__(self,length, cross_section, material):
        super().__init__(length, cross_section, material)
        print('应力计算类')
    def calculate(self):
        """Solves for unknown reaction forces, bending moments, shear forces and deflection

        Uses a sympy.physics.continuum_mechanics.beam.Beam class object to calculate unknown reaction forces, bending
        moment function, shear force function, and deflection function.
        Also creates a symBeam object to generate bending moment, shear force and deflection plots
        :return: None
        """
        E = self.material.TENSILE_MODULUS
        #self.material.TENSILE_MODULUS
        I = self.cross_section.get_area_moment_of_inertia()#这里引入切变模量
        #I = 10
        # create sympy beam object
        self.sympy_beam = sympyBeam(self.length, E, I)
        self.sympy_beam.apply_support = apply_support_fix
        self.apply_loads_to_sympy_beam_object(self.sympy_beam)
        self.sympy_beam.solve_for_reaction_loads(*self.make_reaction_symbols_for_sympy_beam_object(self.sympy_beam))

        # create symbeam object
        self.symbeam_beam = symbeamBeam(self.length)
        self.symbeam_beam.set_young(0, self.length, E)
        self.symbeam_beam.set_inertia(0, self.length, I)
        self.apply_supports_to_symbeam_beam_object()
        self.apply_loads_to_symbeam_beam_object()
        self.symbeam_beam.solve(output=False)
        #fig, ax = self.symbeam_beam.plot()
        #plt.show()
        # calculate the maximum bending moment, shear force and deflection
        self.maxBM = self.calculate_max_bending_moment()
        self.maxSF = self.calculate_max_shear_force()
        self.maxDeflection = self.calculate_max_deflection()

    def calculatestree(self,弯矩,扭矩):
        cwx=self.cross_section.CWX()
        cwn=self.cross_section.CWn()
        self.thy=弯矩/cwx
        self.tx=扭矩/cwn
        self.cross_section.get_area_moment_of_inertiay()
        self.cross_section.get_area_moment_of_inertiap()
        return
    def calculatezhuanjiao(self,切变模量,扭矩):
        cwx=self.cross_section.CWX()
        cwn=self.cross_section.CWn()
        self.jiaodu=57300*扭矩/cwn/切变模量
        self.cross_section.get_area_moment_of_inertiay()
        self.cross_section.get_area_moment_of_inertiap()
        return
if __name__ == '__main__':
    def get_selected_material(self):
        try:
            return self.materialMappings[self.materialSelectionComboBox.currentIndex()]()
        except:
            return None


    class user_beam_supports():
        def __init__(self):
            self.location = 1
            self.supportType = 'fixed'


    from SolidCircularCrossSection import SolidCircularCrossSection

    user_beam_supports1 = user_beam_supports()
    user_beam_supports1 = [("fixed", 10.0)]
    user_beam_supports = user_beam_supports1
    user_beam_loads = [('point', 10.0, 50.0)]
    # print(user_beam_supports.location)
    user_beam_cross_section = SolidCircularCrossSection(10)
    user_beam = beamstress(100, user_beam_cross_section, SteelAISI1045)
    user_beam.set_supports(user_beam_supports)
    user_beam.set_loads(user_beam_loads)
    user_beam.calculate()
