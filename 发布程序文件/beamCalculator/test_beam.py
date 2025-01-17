import unittest, numpy

import pytest

from 程序文件.beamCalculator.Beam.CantileverdBeam import CantileveredBeam
from 程序文件.beamCalculator.Beam.SimplySupportedBeam import SimplySupportedBeam
from 程序文件.beamCalculator.CrossSection.SquareCrossSection import SquareCrossSection
from 程序文件.beamCalculator.Material.SteelAISI1045 import SteelAISI1045
from 程序文件.beamCalculator.Beam.Beam import Beam

@pytest.fixture
def temp_beam():
    temp_beam = Beam(1, SquareCrossSection(0.1), SteelAISI1045())
    temp_beam.add_roller_support(0)
    temp_beam.add_pin_support(1)
    # temp_beam.add_point_load(100, 0.5)
    # temp_beam.add_moment(-100, 0.1)
    #temp_beam.add_udl(100, 0.5, 1, 0)
    return temp_beam

def test_add_udl(temp_beam):
    assert temp_beam.udl == []
    temp_beam.add_udl(100, 0.5, 1, 0)
    assert len(temp_beam.udl) == 1
    assert temp_beam.udl[0].magnitude == 100
    assert temp_beam.udl[0].start_location == 0.5
    assert temp_beam.udl[0].end_location == 1
    assert temp_beam.udl[0].order == 0

def test_calculate():
    test_beam = Beam(1, SquareCrossSection(0.1), SteelAISI1045())
    test_beam.add_roller_support(0)
    test_beam.add_pin_support(1)
    test_beam.add_point_load(100, 0.5)
    test_beam.add_moment(-100, 0.1)
    test_beam.add_udl(100, 0.5, 1, 0)
    assert test_beam.sympy_beam == None
    assert test_beam.symbeam_beam == None
    assert test_beam.maxBM == None
    assert test_beam.maxSF == None
    assert test_beam.maxDeflection == None

    test_beam.calculate()

    assert test_beam.sympy_beam != None
    assert test_beam.symbeam_beam != None
    assert test_beam.maxBM != None
    assert test_beam.maxSF != None
    assert test_beam.maxDeflection != None

    # def test_simplySupportedBeamObjectCreation(self):
    #     test_beam = SimplySupportedBeam(1, SquareCrossSection(0.1), SteelAISI1045())
    #     self.assertEqual(test_beam.length, 1)
    #
    #     #CHECK CROSS-SECTION PROPERTIES
    #     self.assertEqual(test_beam.cross_section.cross_section_type, "Square")
    #
    #     #CHECK MATERIAL PROPERTIES
    #     self.assertEqual(test_beam.material.material_type, "Steel")
    #     self.assertEqual(test_beam.material.DENSITY, 8)
    #     self.assertEqual(test_beam.material.TENSILE_MODULUS, 205)
    #     self.assertEqual(test_beam.material.TENSILE_STRENGTH, 585)
    #
    #
    # def test_add_point_load(self):
    #     test_beam = SimplySupportedBeam(1, SquareCrossSection(0.1), SteelAISI1045())
    #     self.assertTrue(len(test_beam.point_loads) == 0)
    #
    #     #CHECK POINTLOAD OBJECT ADDED TO POINTLOAD LIST
    #     test_beam.add_point_load(100, 0.5)
    #     self.assertTrue(len(test_beam.point_loads) == 1)
    #
    #     #Check force object properties
    #     self.assertEqual(test_beam.point_loads[0].magnitude, 100)
    #     self.assertEqual(test_beam.point_loads[0].start_location, 0.5)
    #
    #     #CHECK CLEAR LOADS FUNCTION
    #     test_beam.clear_loads()
    #     self.assertTrue(len(test_beam.point_loads) == 0)
    #
    # def test_add_support(self):
    #     test_beam = SimplySupportedBeam(1, SquareCrossSection(0.1), SteelAISI1045())
    #     self.assertTrue(len(test_beam.supports) == 0)
    #
    #     #CHECK PIN SUPPORT
    #     test_beam.add_pin_support(0)
    #     self.assertTrue(len(test_beam.supports) == 1)
    #     self.assertEqual(test_beam.supports[0].supportType, "pin")
    #     self.assertEqual(test_beam.supports[0].location, 0)
    #
    #     #CHECK ROLLER SUPPORTS
    #     test_beam.add_roller_support(1)
    #     self.assertTrue(len(test_beam.supports) == 2)
    #     self.assertEqual(test_beam.supports[1].supportType, "roller")
    #     self.assertEqual(test_beam.supports[1].location, 1)
    #
    #     #CHECK CLEAR SUPPORTS
    #     test_beam.clear_supports()
    #     self.assertTrue(len(test_beam.supports) == 0)
    #
    #
    # def test_calculate(self):
    #     test_beam = Beam(1, SquareCrossSection(0.1), SteelAISI1045())
    #     test_beam.add_roller_support(0)
    #     test_beam.add_pin_support(1)
    #     test_beam.add_point_load(100, 0.5)
    #     test_beam.add_moment(-100, 0.1)
    #     test_beam.add_udl(100, 0.5, 1, 0)
    #
    #     assert test_beam.sympy_beam == None
    #     assert test_beam.symbeam_beam == None
    #     assert test_beam.maxBM == None
    #     assert test_beam.maxSF == None
    #     assert test_beam.maxDeflection == None
    #     print("here0")
    #     test_beam.calculate()
    #     print("here")
    #     assert test_beam.sympy_beam != None
    #     assert test_beam.symbeam_beam != None
    #     assert test_beam.maxBM != None
    #     assert test_beam.maxSF != None
    #     assert test_beam.maxDeflection != None
    #
    #
    #
    # def test_cantilever_calculate(self):
    #     test_beam = CantileveredBeam(1, SquareCrossSection(0.1), SteelAISI1045())
    #     self.assertTrue(len(test_beam.supports) == 1)
    #     self.assertEqual(test_beam.supports[0].supportType, "fixed")
    #     test_beam.add_point_load(1000, 1)
    #     test_beam.calculate()
    #
    #     assert test_beam.load_function != None
    #     assert test_beam.bending_moment_function != None
    #     assert test_beam.shear_force_function != None
    #     assert test_beam.deflection_function != None
    #     assert test_beam.free_body_diagram != None


# if __name__ == '__main__':
#     unittest.main()
