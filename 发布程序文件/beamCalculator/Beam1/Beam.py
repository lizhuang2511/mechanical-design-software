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

def convert_to_numpy_piecewise(f):
    """ Coverts sympy Singularity function to a numpy equivalent function.

    This function is used to convert Piecewise sympy Singularity functions for bending moments, shear force and
    deflection into numpy equivalent functions.

    :param f: A sympy Singularity function
    :return: An equivalent function which is compatible with numpy
    """
    x = symbols("x")
    return lambdify(x, f.rewrite(Piecewise), modules='numpy')


def apply_support_fix(self, syms, loc, support_type="fixed"):
    """
    Code from GitHub used to fix the issue where sympy beams would not accept decimal values for support locations
    """
    try:
        reaction_load, reaction_moment = syms
    except:
        try:
            reaction_load, = syms
        except:
            reaction_load = syms
    loc = sympify(loc)
    self._applied_supports.append((loc, support_type))
    if support_type == "pin" or support_type == "roller":
        self.apply_load(reaction_load, loc, -1)
        self.bc_deflection.append((loc, 0))
        print(3)
    else:
        self.apply_load(reaction_load, loc, -1)
        self.apply_load(reaction_moment, loc, -2)
        self.bc_deflection.append((loc, 0))
        self.bc_slope.append((loc, 0))
        self._support_as_loads.append((reaction_moment, loc, -2, None))
    self._support_as_loads.append((reaction_load, loc, -1, None))

from SteelAISI1045 import SteelAISI1045
class Beam:

    def __init__(self, length, cross_section, material):
        """

        :param length: Total beam length
        :type length: int, float
        :param cross_section: The shape of the beam cross-section
        :type cross_section: CrossSection
        :param material: The material type of the beam
        :type material: Material
        """
        self.length = length
        self.cross_section = cross_section
        self.material = material

        self.point_loads = []
        self.moments = []
        self.udl = []
        self.supports = []

        self.sympy_beam = None
        self.symbeam_beam = None

        self.maxBM = None
        self.maxSF = None
        self.maxDeflection = None

        self.load_mappings = {"point": self.add_point_load, "moment": self.add_moment, "udl": self.add_udl}
        self.support_mappings = {"pin": self.add_pin_support, "roller": self.add_roller_support,
                                 "fixed": self.add_fixed_support}

    """
    ** GETTERS AND SETTERS **
    """

    def get_length(self):
        return self.length

    def get_cross_section(self):
        return self.cross_section

    def get_material(self):
        return self.material

    def set_length(self, length):
        self.length = length

    def set_cross_section(self, cross_section):
        self.cross_section = cross_section

    def set_loads(self, loads):
        for load in loads:
            self.add_load(*load)

    def set_supports(self, supports):
        for support in supports:
            self.add_support(*support)

    def set_load_function(self, function):
        self.load_function = function

    def set_bending_moment_function(self, function):
        self.bending_moment_function = function

    def set_shear_force_function(self, function):
        self.shear_force_function = function

    def set_deflection_function(self, function):
        self.deflection_function = function

    def set_free_body_diagram(self, plot_object):
        self.free_body_diagram = plot_object

    def clear_length(self):
        self.length = None

    def clear_cross_section(self):
        self.cross_section = None

    def clear_material(self):
        self.material = None

    def clear_point_loads(self):
        self.point_loads.clear()

    def clear_moments(self):
        self.moments.clear()

    def clear_UDL(self):
        self.udl.clear()

    def clear_supports(self):
        self.supports.clear()

    """
    ********************************
    """

    """
    ** FUNCTIONS FOR FORCES **
    """

    def add_load(self, type_of_load, magnitude, location, end_location=None, order=None):
        self.load_mappings[type_of_load](magnitude, location, end_location)

    def add_point_load(self, magnitude, location, *args):
        new_point_load = PointLoad(magnitude, location)
        self.point_loads.append(new_point_load)

    def add_moment(self, magnitude, location, *args):
        new_moment = Moment(magnitude, location)
        self.moments.append(new_moment)

    def add_udl(self, magnitude, start_location, end_location, order=0):
        new_udl = UDL(magnitude, start_location, end_location, order)
        self.udl.append(new_udl)

    def clear_loads(self):
        self.point_loads.clear()
        self.moments.clear()
        self.udl.clear()

    """
    **************************************
    """

    """
     ** FUNCTIONS FOR SUPPORTS **
    """

    def add_support(self, type_of_support, location):
        self.support_mappings[type_of_support](location)

    def add_pin_support(self, location):
        new_pin_support = PinSupport(location)
        self.supports.append(new_pin_support)

    def add_roller_support(self, location):
        new_roller_support = RollerSupport(location)
        self.supports.append(new_roller_support)

    def add_fixed_support(self, location):
        new_fixed_support = FixedSupport(location)
        self.supports.append(new_fixed_support)

    def clear_supports(self):
        self.supports.clear()

    """
    **************************************
    """

    def calculate(self):
        """Solves for unknown reaction forces, bending moments, shear forces and deflection

        Uses a sympy.physics.continuum_mechanics.beam.Beam class object to calculate unknown reaction forces, bending
        moment function, shear force function, and deflection function.
        Also creates a symBeam object to generate bending moment, shear force and deflection plots
        :return: None
        """
        E = self.material.TENSILE_MODULUS
        I = self.cross_section.get_area_moment_of_inertia()
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
    def wenjianjia(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        return dirs
    def 数据文件夹创建(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        return
    def yulan(self):
        """Solves for unknown reaction forces, bending moments, shear forces and deflection

        Uses a sympy.physics.continuum_mechanics.beam.Beam class object to calculate unknown reaction forces, bending
        moment function, shear force function, and deflection function.
        Also creates a symBeam object to generate bending moment, shear force and deflection plots
        :return: None
        """
        E = 10
        I = 10
        #I = 10
        # create sympy beam object
        self.sympy_beam1 = sympyBeam_1(self.length, E, I)
        self.sympy_beam1.apply_support = apply_support_fix
        self.apply_loads_to_sympy_beam_object(self.sympy_beam1)
        self.make_reaction_symbols_for_sympy_beam_object(self.sympy_beam1)
        #figure, ax = plt.subplots(figsize=(5, 3), ncols=1)
        self.数据文件夹 = self.数据文件夹创建()
        ax = self.sympy_beam1.draw()
        ax.size=[6,2.5]
        path=self.wenjianjia()+'/beampng.png'
        ax.save(path)
        return ax
        #self.sympy_beam.solve_for_reaction_loads(*self.make_reaction_symbols_for_sympy_beam_object(self.sympy_beam))

        # create symbeam object
        '''self.symbeam_beam = symbeamBeam(self.length)
        self.symbeam_beam.set_young(0, self.length, E)
        self.symbeam_beam.set_inertia(0, self.length, I)
        self.apply_supports_to_symbeam_beam_object()
        self.apply_loads_to_symbeam_beam_object()
        self.symbeam_beam.solve(output=False)
        fbd = self.symbeam_beam.plot()
        fbd.show()'''

    def apply_supports_to_symbeam_beam_object(self):
        for support in self.supports:
            self.symbeam_beam.add_support(support.location, support.supportType)

    def apply_loads_to_symbeam_beam_object(self):
        for load in self.point_loads:
            # self.symbeam_beam.add_point_load(load.start_location, load.magnitude)
            self.symbeam_beam.add_point_load(load.start_location,
                                             -1 * load.magnitude)  # negative magnitude to correct for differences in sign convention between the two modules

        for moment in self.moments:
            self.symbeam_beam.add_point_moment(moment.start_location, moment.magnitude)

        for udl in self.udl:
            # self.symbeam_beam.add_distributed_load(udl.start_location, udl.end_location, udl.magnitude * pow(x, udl.order))
            self.symbeam_beam.add_distributed_load(udl.start_location, udl.end_location, (-1 * udl.magnitude) * pow(x,
                                                                                                                    udl.order))  # negative magnitude to correct for differences in sign convention between the two modules

    def apply_loads_to_sympy_beam_object(self, beam):
        for load in self.point_loads:
            beam.apply_load(load.magnitude, load.start_location, -1)

        for moment in self.moments:
            beam.apply_load(moment.magnitude, moment.start_location, -2)

        for udl in self.udl:
            beam.apply_load(udl.magnitude, udl.start_location, udl.order, udl.end_location)

    # def apply_supports_to_sympy_beam_object(self, beam):
    #     for support in self.supports:
    #         beam.apply_support(beam, support.location, support.supportType)

    def make_reaction_symbols_for_sympy_beam_object(self, beam):

        reaction_symbols = []
        for support in self.supports:
            if support.supportType == "fixed":
                symbl = symbols('R_{0}, M_{0}'.format(support.location))
                reaction_symbols.extend(symbl)
                beam.apply_support(beam, symbl, support.location, support.supportType)
            else:
                symbl = symbols('R_{0}'.format(support.location))
                reaction_symbols.append(symbl)
                beam.apply_support(beam, symbl, support.location, support.supportType)
        return reaction_symbols

    def calculate_max_bending_moment(self):
        f = convert_to_numpy_piecewise(self.sympy_beam.bending_moment())
        x_range = np.linspace(0, self.length, 10000)
        return max(f(x_range), key=abs)

    def calculate_max_shear_force(self):
        f = convert_to_numpy_piecewise(self.sympy_beam.shear_force())
        x_range = np.linspace(0, self.length, 10000)
        return max(f(x_range), key=abs)

    def calculate_max_deflection(self):
        f = convert_to_numpy_piecewise(self.sympy_beam.deflection())
        x_range = np.linspace(0, self.length, 10000)
        return max(f(x_range), key=abs)



    """
    ** ABSTRACT METHODS **
    """
    # @abstractmethod
    # def calculate_max_moment(self):
    #     pass
    #
    # @abstractmethod
    # def calculate_moment_at_location_x(self,x):
    #     pass
    #
    # @abstractmethod
    # def calculate_max_deflection(self):
    #     pass
    #
    # @abstractmethod
    # def calculate_deflection_at_location_x(self,x):
    #     pass
    #
    # @abstractmethod
    # def calculate_max_shear_force(self):
    #     pass
    #
    # @abstractmethod
    # def calculate_shear_force_at_location_x(self,x):
    #     pass
    #
    # @abstractmethod
    # def calculate_support_reactions(self):
    #     pass
if __name__=="__main__":
    def get_selected_material(self):
        try:
            return self.materialMappings[self.materialSelectionComboBox.currentIndex()]()
        except:
            return None


    class user_beam_supports():
        def __init__(self):
            self.location=1
            self.supportType='fixed'


    from SolidCircularCrossSection import SolidCircularCrossSection
    user_beam_supports1=user_beam_supports()
    user_beam_supports1=[("fixed", 10.0)]
    user_beam_supports=user_beam_supports1
    user_beam_loads=[('point', 10.0, 50.0)]
    #print(user_beam_supports.location)
    user_beam_cross_section=SolidCircularCrossSection(10)
    user_beam = Beam(100, user_beam_cross_section, SteelAISI1045)
    user_beam.set_supports(user_beam_supports)
    user_beam.set_loads(user_beam_loads)
    user_beam.calculate()