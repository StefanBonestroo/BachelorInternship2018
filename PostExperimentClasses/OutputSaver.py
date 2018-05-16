import GUIFiles.enterInfoGUI as enterInfoGUI

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets

class OutputSaver(QtWidgets.QMainWindow, enterInfoGUI.Ui_enterInfoWindow):

    def __init__(self, parent = None):

        super(OutputSaver, self).__init__(parent)
        self.setupUi(self)

        screen = self.frameGeometry()
        centre = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(centre)
        self.move(screen.topLeft())

#******************************************************************************

        self.conOneRadioButton.clicked.connect(self.makeConditionAvailable)
        self.conTwoRadioButton.clicked.connect(self.makeConditionAvailable)
        self.conThreeRadioButton.clicked.connect(self.makeConditionAvailable)
        self.conFourRadioButton.clicked.connect(self.makeConditionAvailable)


#******************************************************************************

        self.data = None

#******************************************************************************

    def makeConditionAvailable(self):

        one = self.conOneRadioButton.isChecked()
        two = self.conTwoRadioButton.isChecked()
        three = self.conThreeRadioButton.isChecked()
        four = self.conFourRadioButton.isChecked()

        self.conOneLineEdit.setEnabled(one)
        self.conOneLineLabel.setEnabled(one)
        self.conOneFamilyEdit.setEnabled(one)
        self.conOneFamilyLabel.setEnabled(one)
        self.conOneAgeLabel.setEnabled(one)
        self.conOneAgeSpinBox.setEnabled(one)
        self.conOneAgeSpinBox.setEnabled(one)

        self.conTwoLineEdit.setEnabled(two)
        self.conTwoLineLabel.setEnabled(two)
        self.conTwoFamilyEdit.setEnabled(two)
        self.conTwoFamilyLabel.setEnabled(two)
        self.conTwoAgeLabel.setEnabled(two)
        self.conTwoAgeSpinBox.setEnabled(two)
        self.conTwoAgeSpinBox.setEnabled(two)

        self.conThreeLineEdit.setEnabled(three)
        self.conThreeLineLabel.setEnabled(three)
        self.conThreeFamilyEdit.setEnabled(three)
        self.conThreeFamilyLabel.setEnabled(three)
        self.conThreeAgeLabel.setEnabled(three)
        self.conThreeAgeSpinBox.setEnabled(three)
        self.conThreeAgeSpinBox.setEnabled(three)

        self.conFourLineEdit.setEnabled(four)
        self.conFourLineLabel.setEnabled(four)
        self.conFourFamilyEdit.setEnabled(four)
        self.conFourFamilyLabel.setEnabled(four)
        self.conFourAgeLabel.setEnabled(four)
        self.conFourAgeSpinBox.setEnabled(four)
        self.conFourAgeSpinBox.setEnabled(four)

#******************************************************************************
