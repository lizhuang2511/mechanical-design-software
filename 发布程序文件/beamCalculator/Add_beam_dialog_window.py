from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

from Show_dialog_error_messgae_box import showDialogErrorMessageBox


def isValidInputLength(length):
    return float(length) > 0

class Add_beam_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_beam_dialog_window, self).__init__()
        uic.loadUi("../beamCalculator/UiFiles/Add_beam_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.inputted_beam_length = None

    def get_dialog_data(self):
        try:
            length = self.BeamLengthInputField.text()
            if isValidInputLength(length):
                self.inputted_beam_length = float(length)
                self.close()
        except ValueError:
            showDialogErrorMessageBox()
            self.BeamLengthInputField.clear()





