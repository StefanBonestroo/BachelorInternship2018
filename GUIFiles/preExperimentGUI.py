# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preExperimentGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 751)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.preExperimentFrame = QtWidgets.QFrame(self.centralwidget)
        self.preExperimentFrame.setGeometry(QtCore.QRect(60, 10, 1141, 631))
        self.preExperimentFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.preExperimentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preExperimentFrame.setLineWidth(2)
        self.preExperimentFrame.setObjectName("preExperimentFrame")
        self.stimulusFrame = QtWidgets.QFrame(self.preExperimentFrame)
        self.stimulusFrame.setGeometry(QtCore.QRect(10, 10, 441, 301))
        self.stimulusFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stimulusFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stimulusFrame.setObjectName("stimulusFrame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.stimulusFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stimulusTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stimulusTitle.setMaximumSize(QtCore.QSize(53, 16))
        self.stimulusTitle.setObjectName("stimulusTitle")
        self.horizontalLayout_5.addWidget(self.stimulusTitle)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.preStimulusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.preStimulusLabel.setObjectName("preStimulusLabel")
        self.horizontalLayout_4.addWidget(self.preStimulusLabel, 0, QtCore.Qt.AlignHCenter)
        self.preSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.preSpinBox.setMaximum(999)
        self.preSpinBox.setProperty("value", 1)
        self.preSpinBox.setObjectName("preSpinBox")
        self.horizontalLayout_4.addWidget(self.preSpinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stimulusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stimulusLabel.setObjectName("stimulusLabel")
        self.horizontalLayout_3.addWidget(self.stimulusLabel, 0, QtCore.Qt.AlignHCenter)
        self.stimSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.stimSpinBox.setMinimum(1)
        self.stimSpinBox.setMaximum(999)
        self.stimSpinBox.setObjectName("stimSpinBox")
        self.horizontalLayout_3.addWidget(self.stimSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.intervalLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.intervalLabel.setObjectName("intervalLabel")
        self.horizontalLayout.addWidget(self.intervalLabel, 0, QtCore.Qt.AlignHCenter)
        self.interSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.interSpinBox.setMaximum(999)
        self.interSpinBox.setProperty("value", 1)
        self.interSpinBox.setObjectName("interSpinBox")
        self.horizontalLayout.addWidget(self.interSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.numberLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.numberLabel.setObjectName("numberLabel")
        self.horizontalLayout_2.addWidget(self.numberLabel, 0, QtCore.Qt.AlignHCenter)
        self.numberSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.numberSpinBox.setMinimum(1)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.horizontalLayout_2.addWidget(self.numberSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.plotFrame = QtWidgets.QFrame(self.preExperimentFrame)
        self.plotFrame.setGeometry(QtCore.QRect(10, 320, 521, 301))
        self.plotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plotFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plotFrame.setObjectName("plotFrame")
        self.stimulusPlot = QtWidgets.QWidget(self.plotFrame)
        self.stimulusPlot.setGeometry(QtCore.QRect(10, 10, 500, 281))
        self.stimulusPlot.setMaximumSize(QtCore.QSize(500, 281))
        self.stimulusPlot.setObjectName("stimulusPlot")
        self.runAndNotesFrame = QtWidgets.QFrame(self.preExperimentFrame)
        self.runAndNotesFrame.setGeometry(QtCore.QRect(540, 320, 591, 301))
        self.runAndNotesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.runAndNotesFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.runAndNotesFrame.setObjectName("runAndNotesFrame")
        self.layoutWidget = QtWidgets.QWidget(self.runAndNotesFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.notesLabel = QtWidgets.QLabel(self.layoutWidget)
        self.notesLabel.setMaximumSize(QtCore.QSize(36, 16))
        self.notesLabel.setObjectName("notesLabel")
        self.verticalLayout_9.addWidget(self.notesLabel, 0, QtCore.Qt.AlignHCenter)
        self.notesText = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.notesText.setObjectName("notesText")
        self.verticalLayout_9.addWidget(self.notesText)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_9.addWidget(self.line_3)
        self.outputDirectoryText = QtWidgets.QLineEdit(self.layoutWidget)
        self.outputDirectoryText.setReadOnly(True)
        self.outputDirectoryText.setObjectName("outputDirectoryText")
        self.verticalLayout_9.addWidget(self.outputDirectoryText)
        self.setOutputDirectoryButton = QtWidgets.QPushButton(self.layoutWidget)
        self.setOutputDirectoryButton.setObjectName("setOutputDirectoryButton")
        self.verticalLayout_9.addWidget(self.setOutputDirectoryButton)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.runButton = QtWidgets.QPushButton(self.layoutWidget)
        self.runButton.setEnabled(False)
        self.runButton.setMinimumSize(QtCore.QSize(66, 32))
        self.runButton.setObjectName("runButton")
        self.verticalLayout_8.addWidget(self.runButton)
        self.resetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout_8.addWidget(self.resetButton)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.protocolFrame = QtWidgets.QFrame(self.preExperimentFrame)
        self.protocolFrame.setGeometry(QtCore.QRect(460, 10, 671, 301))
        self.protocolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.protocolFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.protocolFrame.setObjectName("protocolFrame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.protocolFrame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(320, 10, 341, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.notRandomRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.notRandomRadioButton.setObjectName("notRandomRadioButton")
        self.verticalLayout_13.addWidget(self.notRandomRadioButton)
        self.randomRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.randomRadioButton.setChecked(True)
        self.randomRadioButton.setObjectName("randomRadioButton")
        self.verticalLayout_13.addWidget(self.randomRadioButton)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cleanChannelLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.cleanChannelLabel.setObjectName("cleanChannelLabel")
        self.horizontalLayout_6.addWidget(self.cleanChannelLabel)
        self.cleanChannelSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.cleanChannelSpinBox.setMaximum(3)
        self.cleanChannelSpinBox.setObjectName("cleanChannelSpinBox")
        self.horizontalLayout_6.addWidget(self.cleanChannelSpinBox)
        self.setCleanChannel = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.setCleanChannel.setObjectName("setCleanChannel")
        self.horizontalLayout_6.addWidget(self.setCleanChannel)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.runtimeErrorLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.runtimeErrorLabel.setFont(font)
        self.runtimeErrorLabel.setLineWidth(2)
        self.runtimeErrorLabel.setText("")
        self.runtimeErrorLabel.setTextFormat(QtCore.Qt.RichText)
        self.runtimeErrorLabel.setScaledContents(True)
        self.runtimeErrorLabel.setObjectName("runtimeErrorLabel")
        self.verticalLayout_12.addWidget(self.runtimeErrorLabel)
        self.connectCameraButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.connectCameraButton.setObjectName("connectCameraButton")
        self.verticalLayout_12.addWidget(self.connectCameraButton)
        self.downloadLastDataButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.downloadLastDataButton.setObjectName("downloadLastDataButton")
        self.verticalLayout_12.addWidget(self.downloadLastDataButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.protocolFrame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 301, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.protocolLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.protocolLabel.setObjectName("protocolLabel")
        self.verticalLayout_11.addWidget(self.protocolLabel, 0, QtCore.Qt.AlignHCenter)
        self.stimulusProtocolList = QtWidgets.QListWidget(self.layoutWidget1)
        self.stimulusProtocolList.setProperty("showDropIndicator", False)
        self.stimulusProtocolList.setDragEnabled(False)
        self.stimulusProtocolList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.stimulusProtocolList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.stimulusProtocolList.setAlternatingRowColors(True)
        self.stimulusProtocolList.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.stimulusProtocolList.setMovement(QtWidgets.QListView.Static)
        self.stimulusProtocolList.setModelColumn(0)
        self.stimulusProtocolList.setObjectName("stimulusProtocolList")
        self.verticalLayout_11.addWidget(self.stimulusProtocolList)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.channelSpinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.channelSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.channelSpinBox.setMaximum(7)
        self.channelSpinBox.setObjectName("channelSpinBox")
        self.horizontalLayout_9.addWidget(self.channelSpinBox)
        self.conditionName = QtWidgets.QLineEdit(self.layoutWidget1)
        self.conditionName.setObjectName("conditionName")
        self.horizontalLayout_9.addWidget(self.conditionName)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.addConditionButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.addConditionButton.setObjectName("addConditionButton")
        self.verticalLayout_11.addWidget(self.addConditionButton)
        self.clearProtocolButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.clearProtocolButton.setObjectName("clearProtocolButton")
        self.verticalLayout_11.addWidget(self.clearProtocolButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frequency Detector"))
        self.stimulusTitle.setText(_translate("MainWindow", "Stimulus"))
        self.preStimulusLabel.setText(_translate("MainWindow", "Pre stimulus (s)"))
        self.stimulusLabel.setText(_translate("MainWindow", "Stimulus (s)"))
        self.intervalLabel.setText(_translate("MainWindow", "Interval (s)"))
        self.numberLabel.setText(_translate("MainWindow", "No. stimulus"))
        self.notesLabel.setText(_translate("MainWindow", "Notes"))
        self.setOutputDirectoryButton.setText(_translate("MainWindow", "Set Directory..."))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Protocol Options"))
        self.notRandomRadioButton.setText(_translate("MainWindow", "Fixed order"))
        self.randomRadioButton.setText(_translate("MainWindow", "Random order"))
        self.cleanChannelLabel.setText(_translate("MainWindow", "Clean Channel:"))
        self.setCleanChannel.setText(_translate("MainWindow", "Set"))
        self.connectCameraButton.setText(_translate("MainWindow", "Connect Camera"))
        self.downloadLastDataButton.setText(_translate("MainWindow", "Download/Save Data"))
        self.protocolLabel.setText(_translate("MainWindow", "Protocol"))
        self.stimulusProtocolList.setSortingEnabled(True)
        self.addConditionButton.setText(_translate("MainWindow", "Add Condition"))
        self.clearProtocolButton.setText(_translate("MainWindow", "Clear"))

