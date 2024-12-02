# @time:2023/4/16 20:10
# Author:lizhuang
# @File:circle_cross_section_dialog_window.py.py
# @Software:PyCharm
from PyQt5 import QtWidgets, uic
import sys
sys.path.append("../Beam")
sys.path.append("../CrossSection")
sys.path.append("../Load")
sys.path.append("../Material")
sys.path.append("../Support")
from SolidCircularCrossSection import SolidCircularCrossSection
from Show_dialog_error_messgae_box import showDialogErrorMessageBox

def isVaildDimension(length):
    return float(length) > 0
class circle_cross_section_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(circle_cross_section_dialog_window, self).__init__()
        uic.loadUi("../beamCalculator/UiFiles/circle_cross_section_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.cross_section_length = None
        self.user_cross_section = None

    def get_dialog_data(self):
        length = self.crossSectionLengthInputField.text()#输入长度值
        try:
            if isVaildDimension(length):
                self.cross_section_length = float(length)
                self.user_cross_section = SolidCircularCrossSection(self.cross_section_length)
                self.close()
        except:
            showDialogErrorMessageBox()
            self.crossSectionLengthInputField.clear()

    def get_user_cross_section(self):
        return self.user_cross_section
