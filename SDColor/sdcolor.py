__author__ = 'Shane DiNozzo'

import sys

# Try to import PyQt5 module. If it is not fount, then the app exits.
try:
    # noinspection PyUnresolvedReferences
    import PyQt5
except ImportError:
    print('PyQt5 module not found! Please install it!')
    exit(0)

# noinspection PyUnresolvedReferences
from PyQt5 import QtWidgets, uic, QtGui, QtCore
# noinspection PyUnresolvedReferences
from PyQt5.QtCore import *
# noinspection PyUnresolvedReferences
from PyQt5.QtGui import *
# noinspection PyUnresolvedReferences
from PyQt5.QtWidgets import QApplication, QStyleFactory

# Load Qt Designer .ui file as GUI for the app
form_class = uic.loadUiType('sdcolor.ui')[0]


class MainWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        sel_color = 0

        # Set window style
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        # Set icon
        self.iconres = QtGui.QPixmap(':/Icon/emblem_money.ico')
        self.icon = QtGui.QIcon(self.iconres)

        # Set button click events
        self.select_color_button.clicked.connect(self.select_color)

    @staticmethod
    def select_color():
        colorpicker = QtWidgets.QColorDialog.getColor()
        myWindow.sel_color = {'r': colorpicker.red(), 'g': colorpicker.green(), 'b': colorpicker.blue(),
                              'h': colorpicker.name()}
        myWindow.rgb_label.setText('RGB:    Red: ' + str(myWindow.sel_color['r']) + '    Green: ' + str(
            myWindow.sel_color['g']) + '    Blue: ' + str(myWindow.sel_color['b']))
        myWindow.hex_label.setText('HEX/HTML: '+myWindow.sel_color['h'])
        myWindow.frame.setStyleSheet("QFrame { background-color: %s }" % myWindow.sel_color['h'])


app = QtWidgets.QApplication(sys.argv)
myWindow = MainWindowClass(None)
myWindow.show()
app.exec()