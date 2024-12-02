from PyQt5 import QtWidgets, uic
import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("../Support")
from SquareCrossSection import SquareCrossSection
from Show_dialog_error_messgae_box import showDialogErrorMessageBox

def isVaildDimension(length):
    return float(length) > 0
class Square_cross_section_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Square_cross_section_dialog_window, self).__init__()
        uic.loadUi("../beamCalculator/UiFiles/Square_cross_section_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.cross_section_length = None
        self.user_cross_section = None

    def get_dialog_data(self):
        length = self.crossSectionLengthInputField.text()
        try:
            if isVaildDimension(length):
                self.cross_section_length = float(length)
                self.user_cross_section = SquareCrossSection(self.cross_section_length)
                self.close()
        except:
            showDialogErrorMessageBox()
            self.crossSectionLengthInputField.clear()

    def get_user_cross_section(self):
        return self.user_cross_section
