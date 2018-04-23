# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postExperimentGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.postExperimentFrame = QtWidgets.QFrame(self.centralwidget)
        self.postExperimentFrame.setGeometry(QtCore.QRect(10, 10, 1431, 511))
        self.postExperimentFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.postExperimentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.postExperimentFrame.setLineWidth(2)
        self.postExperimentFrame.setObjectName("postExperimentFrame")
        self.pickAVideoFrame = QtWidgets.QFrame(self.postExperimentFrame)
        self.pickAVideoFrame.setGeometry(QtCore.QRect(10, 10, 251, 491))
        self.pickAVideoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pickAVideoFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pickAVideoFrame.setObjectName("pickAVideoFrame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.pickAVideoFrame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 231, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pickAVideoLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.pickAVideoLabel.setObjectName("pickAVideoLabel")
        self.verticalLayout_6.addWidget(self.pickAVideoLabel, 0, QtCore.Qt.AlignHCenter)
        self.videoList = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.videoList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.videoList.setObjectName("videoList")
        self.verticalLayout_6.addWidget(self.videoList)
        self.setInputDirectoryButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.setInputDirectoryButton.setObjectName("setInputDirectoryButton")
        self.verticalLayout_6.addWidget(self.setInputDirectoryButton)
        self.videoPreviewFrame = QtWidgets.QFrame(self.postExperimentFrame)
        self.videoPreviewFrame.setGeometry(QtCore.QRect(740, 10, 681, 491))
        self.videoPreviewFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoPreviewFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.videoPreviewFrame.setObjectName("videoPreviewFrame")
        self.videoWidget = VideoPlayer(self.videoPreviewFrame)
        self.videoWidget.setGeometry(QtCore.QRect(0, 0, 671, 471))
        self.videoWidget.setMaximumSize(QtCore.QSize(680, 471))
        self.videoWidget.setObjectName("videoWidget")
        self.optionsFrame = QtWidgets.QFrame(self.postExperimentFrame)
        self.optionsFrame.setGeometry(QtCore.QRect(270, 10, 461, 491))
        self.optionsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.optionsFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.optionsFrame.setObjectName("optionsFrame")
        self.layoutWidget = QtWidgets.QWidget(self.optionsFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 443, 485))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.noiseFrame = QtWidgets.QFrame(self.layoutWidget)
        self.noiseFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.noiseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.noiseFrame.setObjectName("noiseFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.noiseFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.noiseLabel = QtWidgets.QLabel(self.noiseFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.noiseLabel.setFont(font)
        self.noiseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noiseLabel.setObjectName("noiseLabel")
        self.verticalLayout_3.addWidget(self.noiseLabel)
        self.middleFrameCheckBox = QtWidgets.QCheckBox(self.noiseFrame)
        self.middleFrameCheckBox.setAutoExclusive(False)
        self.middleFrameCheckBox.setObjectName("middleFrameCheckBox")
        self.verticalLayout_3.addWidget(self.middleFrameCheckBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gaussianCheckBox = QtWidgets.QCheckBox(self.noiseFrame)
        self.gaussianCheckBox.setObjectName("gaussianCheckBox")
        self.horizontalLayout_3.addWidget(self.gaussianCheckBox)
        self.useBlankCheckBox = QtWidgets.QCheckBox(self.noiseFrame)
        self.useBlankCheckBox.setObjectName("useBlankCheckBox")
        self.horizontalLayout_3.addWidget(self.useBlankCheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.noiseFrame)
        self.featureFrame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.featureFrame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.featureFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.featureFrame_2.setObjectName("featureFrame_2")
        self.featureFrame = QtWidgets.QVBoxLayout(self.featureFrame_2)
        self.featureFrame.setObjectName("featureFrame")
        self.featureLabel = QtWidgets.QLabel(self.featureFrame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.featureLabel.setFont(font)
        self.featureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.featureLabel.setObjectName("featureLabel")
        self.featureFrame.addWidget(self.featureLabel)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.thresholdLabel = QtWidgets.QLabel(self.featureFrame_2)
        self.thresholdLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.horizontalLayout_4.addWidget(self.thresholdLabel)
        self.thresholdSpinBox = QtWidgets.QSpinBox(self.featureFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSpinBox.sizePolicy().hasHeightForWidth())
        self.thresholdSpinBox.setSizePolicy(sizePolicy)
        self.thresholdSpinBox.setMinimum(1)
        self.thresholdSpinBox.setProperty("value", 10)
        self.thresholdSpinBox.setObjectName("thresholdSpinBox")
        self.horizontalLayout_4.addWidget(self.thresholdSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dilationLabel = QtWidgets.QLabel(self.featureFrame_2)
        self.dilationLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dilationLabel.setObjectName("dilationLabel")
        self.horizontalLayout_5.addWidget(self.dilationLabel)
        self.dilationSpinBox = QtWidgets.QSpinBox(self.featureFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dilationSpinBox.sizePolicy().hasHeightForWidth())
        self.dilationSpinBox.setSizePolicy(sizePolicy)
        self.dilationSpinBox.setMinimum(0)
        self.dilationSpinBox.setProperty("value", 2)
        self.dilationSpinBox.setObjectName("dilationSpinBox")
        self.horizontalLayout_5.addWidget(self.dilationSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.featureFrame.addLayout(self.verticalLayout_7)
        self.verticalLayout.addWidget(self.featureFrame_2)
        self.outputAnalysisFrame = QtWidgets.QFrame(self.layoutWidget)
        self.outputAnalysisFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.outputAnalysisFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputAnalysisFrame.setObjectName("outputAnalysisFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.outputAnalysisFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.outputAnalysisFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.previewOutputButton = QtWidgets.QPushButton(self.outputAnalysisFrame)
        self.previewOutputButton.setObjectName("previewOutputButton")
        self.verticalLayout_5.addWidget(self.previewOutputButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameNumberSpinBox = QtWidgets.QSpinBox(self.outputAnalysisFrame)
        self.frameNumberSpinBox.setMinimum(1)
        self.frameNumberSpinBox.setMaximum(100000)
        self.frameNumberSpinBox.setObjectName("frameNumberSpinBox")
        self.verticalLayout_4.addWidget(self.frameNumberSpinBox)
        self.checkFrameButton = QtWidgets.QPushButton(self.outputAnalysisFrame)
        self.checkFrameButton.setObjectName("checkFrameButton")
        self.verticalLayout_4.addWidget(self.checkFrameButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.outputAnalysisFrame)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.roiLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roiLabel.sizePolicy().hasHeightForWidth())
        self.roiLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roiLabel.setFont(font)
        self.roiLabel.setLineWidth(1)
        self.roiLabel.setMidLineWidth(0)
        self.roiLabel.setScaledContents(False)
        self.roiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.roiLabel.setWordWrap(True)
        self.roiLabel.setObjectName("roiLabel")
        self.verticalLayout_2.addWidget(self.roiLabel)
        self.roiListWidget = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roiListWidget.sizePolicy().hasHeightForWidth())
        self.roiListWidget.setSizePolicy(sizePolicy)
        self.roiListWidget.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.roiListWidget.setFont(font)
        self.roiListWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.roiListWidget.setObjectName("roiListWidget")
        self.verticalLayout_2.addWidget(self.roiListWidget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectRoiButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectRoiButton.sizePolicy().hasHeightForWidth())
        self.selectRoiButton.setSizePolicy(sizePolicy)
        self.selectRoiButton.setObjectName("selectRoiButton")
        self.horizontalLayout.addWidget(self.selectRoiButton)
        self.clearRoiButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearRoiButton.setObjectName("clearRoiButton")
        self.horizontalLayout.addWidget(self.clearRoiButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.runAnalysisButton = QtWidgets.QPushButton(self.layoutWidget)
        self.runAnalysisButton.setObjectName("runAnalysisButton")
        self.verticalLayout_15.addWidget(self.runAnalysisButton)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stopAnalysisButton = QtWidgets.QPushButton(self.layoutWidget)
        self.stopAnalysisButton.setFlat(False)
        self.stopAnalysisButton.setObjectName("stopAnalysisButton")
        self.horizontalLayout_8.addWidget(self.stopAnalysisButton)
        self.saveOutputButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveOutputButton.setObjectName("saveOutputButton")
        self.horizontalLayout_8.addWidget(self.saveOutputButton)
        self.verticalLayout_15.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_15)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.progressLabel = QtWidgets.QLabel(self.layoutWidget)
        self.progressLabel.setText("")
        self.progressLabel.setObjectName("progressLabel")
        self.verticalLayout_14.addWidget(self.progressLabel, 0, QtCore.Qt.AlignHCenter)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_14.addWidget(self.progressBar)
        self.verticalLayout_10.addLayout(self.verticalLayout_14)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 530, 1431, 421))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.frequencyPlot = QtWidgets.QWidget(self.frame_2)
        self.frequencyPlot.setGeometry(QtCore.QRect(10, 10, 591, 401))
        self.frequencyPlot.setObjectName("frequencyPlot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pickAVideoLabel.setText(_translate("MainWindow", "Pick a video to analyze"))
        self.videoList.setSortingEnabled(True)
        self.setInputDirectoryButton.setText(_translate("MainWindow", "Set Directory..."))
        self.noiseLabel.setText(_translate("MainWindow", "Noise reduction"))
        self.middleFrameCheckBox.setText(_translate("MainWindow", "Average difference-frames"))
        self.gaussianCheckBox.setText(_translate("MainWindow", "Gaussian"))
        self.useBlankCheckBox.setText(_translate("MainWindow", "Last ROI = blank"))
        self.featureLabel.setText(_translate("MainWindow", "Feature Enhancement"))
        self.thresholdLabel.setText(_translate("MainWindow", "Pixel threshold"))
        self.dilationLabel.setText(_translate("MainWindow", "Dilation"))
        self.label.setText(_translate("MainWindow", "Output"))
        self.previewOutputButton.setText(_translate("MainWindow", "Preview"))
        self.checkFrameButton.setText(_translate("MainWindow", "Show Frame"))
        self.roiLabel.setText(_translate("MainWindow", "ROI = (up-left x, up-left y, width, height)"))
        self.selectRoiButton.setText(_translate("MainWindow", "Select ROI"))
        self.clearRoiButton.setText(_translate("MainWindow", "Clear"))
        self.runAnalysisButton.setText(_translate("MainWindow", "Run Analysis"))
        self.stopAnalysisButton.setText(_translate("MainWindow", "Stop Analysis"))
        self.saveOutputButton.setText(_translate("MainWindow", "Save Output"))

from PostExperimentClasses.VideoPlayer import VideoPlayer
