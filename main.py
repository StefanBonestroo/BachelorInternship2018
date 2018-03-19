"""
main.py

This is the main application.

created by: Stefan Bonestroo
date created: 07/02/2018
date last modified: 13/03/2018

"""

import sys


from HomeScreen import HomeScreen

from PyQt5 import QtCore, QtGui, QtWidgets

def main():

    # The application will be run as a QApplication
    app = QtWidgets.QApplication(sys.argv)

    # 'homeScreen' will be a GUI object and will be presented
    homeScreen = HomeScreen()
    homeScreen.show()

    if not app.exec_():

        homeScreen.close()

        if homeScreen.choice == "Experiment":

            from PreExperimentClasses.GUI import GUI as preGUI

            pre = preGUI()
            pre.show()
            app.exec_()

        else:

            from PostExperimentClasses.GUI import GUI as postGUI

            post = postGUI()
            post.show()
            app.exec_()


if __name__ == '__main__':
    main()
