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
        MainWindow.resize(321, 198)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ExperimentOrAnalysisLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExperimentOrAnalysisLabel.sizePolicy().hasHeightForWidth())
        self.ExperimentOrAnalysisLabel.setSizePolicy(sizePolicy)
        self.ExperimentOrAnalysisLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ExperimentOrAnalysisLabel.setAlignment(QtCore.Qt.AlignCenter)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.ExperimentOrAnalysisLabel.setText(_translate("MainWindow", "Pick an option:"))
        self.experimentButton.setText(_translate("MainWindow", "Experiment"))
        self.analysisButton.setText(_translate("MainWindow", "Analysis"))

