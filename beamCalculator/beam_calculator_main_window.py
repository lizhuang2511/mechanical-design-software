#!/usr/bin/python
import traceback
import os
from PyQt5 import QtWidgets, uic, Qt
import os
import sys
import tkinter
from mohr import Calculations,Gui33
import tkinter
import tkinter.messagebox
import math
import sys
import os
import subprocess
sys.path.append("../beamCalculator/Beam1")
sys.path.append("../beamCalculator/CrossSection1")
sys.path.append("../beamCalculator/Load1")
sys.path.append("../beamCalculator/Material1")
sys.path.append("../beamCalculator/Support1")
from Add_UDL_dialog_window import Add_UDL_dialog_window
from Add_beam_dialog_window import Add_beam_dialog_window
from Add_moment_dialog_window import Add_moment_dialog_window
from Add_support_dialog_window import Add_support_dialog_window
from Add_pointLoad_dialog_window import Add_pointLoad_dialog_window
from Rectangular_cross_section_dialog_window1 import Rectangular_cross_section_dialog_window
from circle_cross_section_dialog_window import circle_cross_section_dialog_window
from Reset_dialog_window import Reset_dialog_window
from Show_dialog_error_messgae_box import showDialogErrorMessageBox
from Solution_summary_dialog_window import Solution_summary_dialog_window
from Square_cross_section_dialog_window import Square_cross_section_dialog_window
from open_streesolve_dialog_window import open_streesolve_dialog_window
from SteelAISI1045 import SteelAISI1045
from CastIronGrade20 import CastIronGrade20
from Beam import Beam
from 应力计算 import beamstress
import matplotlib
#matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
#from ..definitions import UI_FILES_DIR


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi(r'..\beamCalculator\UiFiles\beam_calculator_main_window.ui',self)

        self.crossSectionComboBoxDialogWindowMappings = {0: None,
                                                         1: self.open_circle_cross_section_dialog_window,
                                                         2: self.open_square_cross_section_dialog_window,
                                                         3: self.open_rectangular_cross_section_dialog_window}
        self.materialMappings = {0: None, 1: SteelAISI1045, 2: CastIronGrade20}

        # Properties of the users beam used for calculation
        self.user_beam_length = None
        self.user_beam_cross_section = None
        self.user_beam_loads = []
        self.user_beam_supports = []

        # Users beam object
        self.user_beam = None

        # Define click event actions for buttons
        self.addBeamButton.clicked.connect(self.open_add_beam_window)
        self.addSupportButton.clicked.connect(self.open_add_support_window)
        self.addPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
        self.addMomentButton.clicked.connect(self.open_add_moment_window)
        self.addUDLButton.clicked.connect(self.open_add_udl_window)
        self.crossSectionSelectionComboBox.currentIndexChanged.connect(self.open_cross_section_dialog_window)
        self.solveButton.clicked.connect(self.solve)
        self.resetButton.clicked.connect(self.open_reset_dialog_window)
        from fuzhuui import fuzhuui
        self.fuzhuui1 = fuzhuui()
    def clear_user_beam_length(self):
        self.user_beam_length = None

    def clear_user_beam_cross_section(self):
        self.user_beam_cross_section = None
        self.crossSectionSelectionComboBox.setCurrentIndex(0)

    def clear_user_beam_point_loads(self):
        self.user_beam_loads = [l for l in self.user_beam_loads if l[0] != 'point']

    def clear_user_beam_moments(self):
        self.user_beam_loads = [l for l in self.user_beam_loads if l[0] != 'moment']

    def clear_user_beam_udl(self):
        self.user_beam_loads = [l for l in self.user_beam_loads if l[0] != 'udl']

    def clear_user_beam_supports(self):
        self.user_beam_supports.clear()

    def clear_user_beam_material(self):
        self.materialSelectionComboBox.setCurrentIndex(0)

    def open_add_beam_window(self):  # Group into one open_dialog_window function with a dialog.UiFiles parameter
        self.dialog = Add_beam_dialog_window()
        self.dialog.exec_()
        self.user_beam_length = self.dialog.inputted_beam_length

    def open_add_support_window(self):
        self.dialog = Add_support_dialog_window()
        self.dialog.exec_()
        if is_all_support_data_present(self.dialog):
            self.user_beam_supports.append((self.dialog.support_type, self.dialog.support_location))#添加

    def open_add_pointLoad_window(self):
        try:
             self.dialog = Add_pointLoad_dialog_window(load=self.fuzhuui1.载荷)
             self.dialog.exec_()
        except:
             self.dialog = Add_pointLoad_dialog_window()
             self.dialog.exec_()
        if is_all_point_load_dialog_data_present(self.dialog):
            self.user_beam_loads.append(
                ("point", self.dialog.inputted_load_magnitude, self.dialog.inputted_load_location))

    def open_add_moment_window(self):
        self.dialog = Add_moment_dialog_window()
        self.dialog.exec_()
        if is_all_moment_dialog_data_present(self.dialog):
            self.user_beam_loads.append(
                ("moment", self.dialog.inputted_load_magnitude, self.dialog.inputted_load_location))

    def open_add_udl_window(self):
        self.dialog = Add_UDL_dialog_window()
        self.dialog.exec_()
        if is_all_udl_dialog_window_data_present(self.dialog):
            self.user_beam_loads.append(("udl", self.dialog.inputted_load_magnitude,
                                         self.dialog.inputted_load_start_location,
                                         self.dialog.inputted_load_end_location, self.dialog.inputted_load_order))

    def open_cross_section_dialog_window(self):
        idx = self.crossSectionSelectionComboBox.currentIndex()
        if idx != 0:
            self.crossSectionComboBoxDialogWindowMappings[idx]()

    def open_rectangular_cross_section_dialog_window(self):
        self.dialog = Rectangular_cross_section_dialog_window()
        self.dialog.exec_()
        self.user_beam_cross_section = self.dialog.get_user_cross_section()
    def open_circle_cross_section_dialog_window(self):
        self.dialog = circle_cross_section_dialog_window()
        self.dialog.exec_()
        self.user_beam_cross_section = self.dialog.get_user_cross_section()

    def open_square_cross_section_dialog_window(self):
        self.dialog = Square_cross_section_dialog_window()
        self.dialog.exec_()
        self.user_beam_cross_section = self.dialog.get_user_cross_section()

    def open_solution_summary_dialog_window(self):
        self.dialog = Solution_summary_dialog_window(self.user_beam)
        self.dialog.show()
    def open_streesolve_dialog_window(self):
        try:
            self.dialog = open_streesolve_dialog_window(self.user_beam2,niuju=self.fuzhuui1.扭矩)
            self.dialog.lineEdit_3.setText(str(int(self.user_beam2.maxBM)))
            self.dialog.show()
        except:
            self.dialog = open_streesolve_dialog_window(self.user_beam2, )
            self.dialog.lineEdit_3.setText(str(int(self.user_beam2.maxBM)))
            self.dialog.show()
    def open_reset_dialog_window(self):
        self.dialog = Reset_dialog_window(self)
        self.dialog.exec_()

    def get_selected_material(self):
        try:
            return self.materialMappings[self.materialSelectionComboBox.currentIndex()]()
        except:
            return None

    def get_selected_cross_section(self):
        pass
    def wenjianjia(self):
        import os
        桌面 = os.path.join(os.path.expanduser("~"), 'Desktop')
        dirs = 桌面 + '/数据文件'
        return dirs
    def draw2(self):
        from PyQt5.QtGui import QPixmap
        print('预览')
        try:
            if self.yulanis_valid_beam_input():
                self.user_beam = Beam(self.user_beam_length, None,None)
                self.user_beam.set_supports(self.user_beam_supports)
                self.user_beam.set_loads(self.user_beam_loads)
                ax=self.user_beam.yulan()
                print(type(ax))
                path=self.wenjianjia()+'/beampng.png'
                self.graphicscene = QtWidgets.QGraphicsScene()
                self.label_5.setPixmap(QPixmap(path))
            else:
                raise InvalidBeamInputException
        except:
            traceback.print_exc()
            showDialogErrorMessageBox()
            '''self.graphicscene.addWidget(ax)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
            self.graphicsView.setScene(self.graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
            self.graphicsView.show()  # 最后，调用show方法呈现图形！'''
            '''else:
                raise InvalidBeamInputException'''
        return
    def solve(self):
        try:
            if self.is_valid_beam_input():
                self.user_beam = Beam(self.user_beam_length, self.user_beam_cross_section, self.get_selected_material())
                self.user_beam.set_supports(self.user_beam_supports)
                self.user_beam.set_loads(self.user_beam_loads)
                self.user_beam.calculate()
                self.open_solution_summary_dialog_window()
            else:
                raise InvalidBeamInputException
        except:
            traceback.print_exc()
            showDialogErrorMessageBox()
    def stresssolve(self):
        try:
            if self.is_valid_beam_input():
                self.user_beam2 = beamstress(self.user_beam_length, self.user_beam_cross_section, self.get_selected_material())
                self.user_beam2.set_supports(self.user_beam_supports)
                self.user_beam2.set_loads(self.user_beam_loads)
                self.user_beam2.calculate()
                self.open_streesolve_dialog_window()
            else:
                raise InvalidBeamInputException
        except:
            traceback.print_exc()
            showDialogErrorMessageBox()
    def moeryuan(self):
        import pandas as pd
        cc=pd.read_csv(self.wenjianjia()+'/弯扭距.csv')
        app1 = tkinter.Tk()
        Gui33(app1,int(cc['wan'].values),int(cc['niu'].values))
        app1.mainloop()
        return
    def is_valid_beam_input(self):
        if None in [self.user_beam_length, self.user_beam_cross_section, self.get_selected_material()] or len(
                self.user_beam_loads) == 0 or len(self.user_beam_supports) == 0:
            return False
        return True
    def yulanis_valid_beam_input(self):
        if None in [self.user_beam_length] :
            return False
        return True
    def fuzhujiemian(self):
        self.fuzhuui1.show()
        return

def is_all_support_data_present(dialog):
    return not None in [dialog.support_type, dialog.support_location]


def is_all_point_load_dialog_data_present(dialog):
    return not None in [dialog.inputted_load_location, dialog.inputted_load_magnitude]


def is_all_moment_dialog_data_present(dialog):
    return not None in [dialog.inputted_load_location, dialog.inputted_load_magnitude]


def is_all_udl_dialog_window_data_present(dialog):
    return not None in [dialog.inputted_load_magnitude, dialog.inputted_load_start_location,
                        dialog.inputted_load_end_location, dialog.inputted_load_order]


class InvalidBeamInputException(Exception):
    pass


if __name__ == "__main__":
    import sys
    import pandas as pd
    #cc = pd.read_csv(self.wenjianjia() + '/弯扭距.csv')
    #app1 = tkinter.Tk()
    #Gui33(app1, int(5), int(5))
    #app1.mainloop()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())
