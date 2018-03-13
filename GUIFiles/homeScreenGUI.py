# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScreenGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 130, 401, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ExperimentOrAnalysisLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ExperimentOrAnalysisLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ExperimentOrAnalysisLabel.setObjectName("ExperimentOrAnalysisLabel")
        self.verticalLayout.addWidget(self.ExperimentOrAnalysisLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.experimentButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.experimentButton.setObjectName("experimentButton")
        self.horizontalLayout.addWidget(self.experimentButton)
        self.analysisButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.analysisButton.setObjectName("analysisButton")
        self.horizontalLayout.addWidget(self.analysisButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ExperimentOrAnalysisLabel.setText(_translate("MainWindow", "What would you like to do?"))
        self.experimentButton.setText(_translate("MainWindow", "Experiment"))
        self.analysisButton.setText(_translate("MainWindow", "Analysis"))

