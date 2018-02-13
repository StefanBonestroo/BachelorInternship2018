"""
main.py

This is the main application.

created by: Stefan Bonestroo
date created: 07/02/2018
date last modified: 08/02/2018

"""

import sys

import design
from Classes.GUI import GUI
from PyQt5 import QtCore, QtGui, QtWidgets

def main():

    # The application will be run as a QApplication
    app = QtWidgets.QApplication(sys.argv)

    # 'mainscreen' will be a GUI object and will be presented
    mainScreen = GUI()
    mainScreen.showFullScreen()
    app.exec_()

if __name__ == '__main__':
    main()
