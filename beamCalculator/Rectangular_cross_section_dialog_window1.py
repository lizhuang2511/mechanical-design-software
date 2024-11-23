from PyQt5 import QtWidgets, uic
import sys
sys.path.append("../beamCalculator/Beam")
sys.path.append("../beamCalculator/CrossSection")
sys.path.append("../beamCalculator/Load")
sys.path.append("../beamCalculator/Material")
sys.path.append("../beamCalculator/Support")
sys.path.append("../beamCalculator")
from RectangularCrossSection import RectangularCrossSection
from Show_dialog_error_messgae_box import showDialogErrorMessageBox

def isVaildDimensions(width, height):
    return float(width) > 0 and float(height) > 0
class Rectangular_cross_section_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Rectangular_cross_section_dialog_window, self).__init__()
        uic.loadUi("../beamCalculator/UiFiles/Rectangular_cross_section_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.cross_section_length = self.cross_section_width = None
        self.user_cross_section = None

    def get_dialog_data(self):
        try:
            width, height = self.crossSectionWidthInputField.text(), self.crossSectionLengthInputField.text()
            if isVaildDimensions(width, height):
                self.cross_section_width = float(width)
                self.cross_section_length = float(height)
                self.user_cross_section = RectangularCrossSection(self.cross_section_width, self.cross_section_length)
                self.close()
        except:
            showDialogErrorMessageBox()
            self.crossSectionWidthInputField.clear()
            self.crossSectionLengthInputField.clear()

    def get_user_cross_section(self):
        return self.user_cross_section
