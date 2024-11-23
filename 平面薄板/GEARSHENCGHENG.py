#!/usr/bin/python
# coding: utf-8

"""Example problem 1 for pyGear

Summary
-------
Create gear geometry and a export STEP file

"""

from __future__ import print_function

import pygear
import example_data
extgear_2 = {'m_n': 10.0, 'z': 11, 'beta': 0,'x': 0.35, 'alpha_n': 20.0, 'b': 180,  'd_s': 20.0}
geardata =extgear_2  # select gear data here
mygear = pygear.CylindricalGearWheel(geardata)  # create cylindrical gear wheel instance
print(mygear)  # print gear data
mygear_solid = mygear.makeOCCSolid()  # create OCC-3d-solid of gear wheel

# write 3d-solid of gear to STEP-file (in working directory)
pygear.writeOCCShape(mygear_solid, 'extgear_1.stp', 'step')

# write 3d-solid of gear to IGES-file (in working directory), IGES interface has bug!
pygear.writeOCCShape(mygear_solid, 'extgear_1.igs', 'iges')

# write 3d-solid of gear to VRML-file (in working directory)
pygear.writeOCCShape(mygear_solid, 'extgear_1.wrl', 'vrml')
pygear.displayOCCShape(mygear_solid)