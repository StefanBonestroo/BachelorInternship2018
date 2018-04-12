import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets

import GUIFiles.homeScreenGUI

class HomeScreen(QtWidgets.QMainWindow, GUIFiles.homeScreenGUI.Ui_MainWindow):

    def __init__(self, parent = None):

        # This tells GUI to inherit everything initiated by the design.py file
        # which contains all information about the front-end of the GUI
        super(HomeScreen, self).__init__(parent)
        self.setupUi(self)

        self.experimentButton.clicked.connect(self.experimentChosen)
        self.analysisButton.clicked.connect(self.analysisChosen)

        self.choice = None

        frame = self.frameGeometry()
        centre = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(centre)
        self.move(frame.topLeft())

    def experimentChosen(self):

        self.choice = "Experiment"
        QtWidgets.QApplication.quit()

    def analysisChosen(self):

        self.choice = "Analysis"
        QtWidgets.QApplication.quit()
