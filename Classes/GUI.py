"""
GUI.py

The class in this file describes the Graphical User Interface (GUI) with all the possible
interactions a user can have with it.

created by: Stefan Bonestroo
date created: 08/02/2018
date last modified: 07/02/2018
"""

import os
import sys
import random
import time
import threading

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets

import design
from Classes.StimulusPlot import StimulusPlotCanvas
from Classes.VideoProcessor import VideoProcessor
from Classes.Controller import DeviceController
from Classes.VideoPlayer import VideoPlayer

class GUI(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent = None):

        # This tells GUI to inherit everything initiated by the design.py file
        # which contains all information about the front-end of the GUI
        super(GUI, self).__init__(parent)
        self.setupUi(self)

#******************************************************************************

        # Triggers 'setInputDirectory' on the button press
        self.setInputDirectoryButton.clicked.connect(self.setInputDirectory)
        self.videoDirectory = None

#******************************************************************************

        # A box is placed that will hold the canvas for the stimulus plot, and
        # the canvas is initiated.
        self.box = QtWidgets.QVBoxLayout(self.stimulusPlot)
        self.graph = StimulusPlotCanvas(self.stimulusPlot, width = 5, height = 4, dpi = 100)
        self.box.addWidget(self.graph)

#******************************************************************************

        # The user can append a stimulus protocol to these arrays
        self.channelsTaken = []
        self.conditions = []

        # Updates the stimulus plot to show a standard stimulus protocol
        self.updateStimulusPlot()

#******************************************************************************

        # When the values of the stimulus protocol change, 'updateStimulusPlot'
        # will trigger
        self.preSpinBox.valueChanged.connect(self.updateStimulusPlot)
        self.stimSpinBox.valueChanged.connect(self.updateStimulusPlot)
        self.interSpinBox.valueChanged.connect(self.updateStimulusPlot)
        self.numberSpinBox.valueChanged.connect(self.updateStimulusPlot)

#******************************************************************************

        self.addConditionButton.clicked.connect(self.addToProtocol)
        self.clearProtocolButton.clicked.connect(self.clearProtocol)

        self.testStimulusButton.clicked.connect(self.testStimulus)

#******************************************************************************

        self.autoNamingCheckbox.stateChanged.connect(self.autoNamingChange)

        self.setOutputDirectoryButton.clicked.connect(self.setOutputDirectory)

#******************************************************************************

        # Timer for the little stimulus bleep
        self.bleepTimer = QtCore.QTimer()
        self.bleepTimer.timeout.connect(self.graph.bleepShower)

#******************************************************************************

        self.runButton.clicked.connect(self.runExperiment)
        self.cancelButton.clicked.connect(self.terminateExperiment)

        self.deviceController = None
        self.updateController()

#******************************************************************************

        self.runAnalysisButton.clicked.connect(self.runAnalysis)
        self.processor = None

#******************************************************************************

        self.videoPath = None

        self.videoBox = QtWidgets.QVBoxLayout(self.videoWidget)
        self.player = VideoPlayer()
        self.videoBox.addWidget(self.player)
        self.videoList.currentItemChanged.connect(self.videoPathChanged)

#******************************************************************************

    """
    This function lets the user pick a directory and will present all relevant
    files inside a QListWidget (video files in our case).
    """
    def setInputDirectory(self):

        # The list is cleared
        self.videoList.clear()

        # A directory picker is opened
        self.videoDirectory = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose your directory")

        # If a directory has been chosen, iterate over all files en add all videofiles to the list
        if self.videoDirectory:

            for video in os.listdir(self.videoDirectory):

                if video.endswith(".mov") or video.endswith(".mp4"):

                    self.videoList.addItem(video)

#******************************************************************************

    """
    This function will use the info from the spinboxes to construct
    a stimulus plot to be viewed inside of the canvas.
    """
    def updateStimulusPlot(self):

        # The spinbox values are obtained
        pre = self.preSpinBox.value()
        stimulus = self.stimSpinBox.value()
        interval = self.interSpinBox.value()
        amountOfStimuli = self.numberSpinBox.value()

        x = [0]
        y = [0]

        # The course of the stimulus plot will be put into a list, so we can plot from it
        x.append(pre)
        y.append(1)

        time = pre

        # Since a stimulus can be presented multiple times, the same combo of
        # stimulus + interval will be pasted n ('amountOfStimuli') times
        for repeat in range(amountOfStimuli):

            time += stimulus
            x.append(time)
            y.append(0)

            time += interval
            x.append(time)
            y.append(1)

        # The last value of y should be 0, so that the plot looks nice
        y[len(y) - 1] = 0

        # Also a 'nice'-maker
        if stimulus == 0:
            y = [0] * len(y)

        # Tells the canvas what the values of x and y are
        self.graph.x = x
        self.graph.y = y

        # Tells the canvas to plot the stimulus and present it
        self.graph.plotStimulus()
        self.graph.draw()

        if len(self.channelsTaken) > amountOfStimuli:

            self.stimulusProtocolList.takeItem(amountOfStimuli)

            self.conditions = self.conditions[:-1]
            self.channelsTaken = self.channelsTaken[:-1]

#******************************************************************************

    """
    This function populates the stimulus protocol list with conditions entered by
    the user. A condition is a condition name and a output channel number.
    """

    def addToProtocol(self):

        channel = str(self.channelSpinBox.value())
        condition = self.conditionName.text()

        item = channel + "    - " + condition

        # The user can only enter as much conditions as there are stimuli
        # Also, a already taken channel cannot be picked
        if channel not in self.channelsTaken and \
            len(self.channelsTaken) < self.numberSpinBox.value():

            self.stimulusProtocolList.addItem(item)
            self.channelsTaken.append(channel)

            self.conditions.append(condition)
            self.graph.conditionLabels.append(condition)

            # Automatic channel increment
            self.channelSpinBox.setValue(self.channelSpinBox.value() + 1)

            self.stimulusProtocolList.setCurrentRow(0)

            self.updateStimulusPlot()

#******************************************************************************

    """
    This function enables the user to test out a stimulus.
    """

    def testStimulus(self):

        if len(self.conditions) is not 0:

            index = self.stimulusProtocolList.currentRow()
            print(self.conditions[index])


#******************************************************************************

    """
    This function clears the stimulus protocol list.
    """

    def clearProtocol(self):

            self.stimulusProtocolList.clear()

            self.channelsTaken = []
            self.conditions = []

            self.graph.conditionLabels = []
            self.updateStimulusPlot()

#******************************************************************************

    """
    This function enables/disables custom file names.
    """

    def autoNamingChange(self):

        # The video name text field is read-only if the box is checked, and
        # will not be used when this is the case
        self.videoNameText.setReadOnly(self.autoNamingCheckbox.checkState())

#******************************************************************************

    """
    This function changes the path where the output will be saved in.
    """
    def setOutputDirectory(self):

        # A directory picker is opened
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose your directory")

        self.outputDirectoryText.setText(directory)

#******************************************************************************

    """
    This function will run 'plotStimulus' under different conditions, since the
    stimulusplot is already constructed. This merely controls the little bleep.
    """
    def runExperiment(self):

        self.updateController()

        # The last value of the x list will be the total running time
        self.graph.runningTime = self.graph.x[len(self.graph.x) - 1]

        # This initiates the deviceController thread, so visualizations and the
        # stimulus protocol can be run at the same time
        self.deviceController.start()

        time.sleep(15)

        # The connection that this timer has will be executed every 'bleepInterval'
        # milliseconds. This means that 'bleepShower' is triggered every 'bleepInterval' ms
        self.bleepTimer.start(self.graph.bleepInterval)




#******************************************************************************

    """
    This function will terminate an experiment run.
    """
    def terminateExperiment(self):

        self.bleepTimer.stop()

        self.graph.resetStuff()
        self.updateStimulusPlot()

#******************************************************************************

    """
    This function runs the analysis of the selected video material when 'Run Analysis'
    is pressed.
    """
    def runAnalysis(self):

        text = "Preparing frame grabber..."
        self.progressLabel.setText(text)
        self.progressBar.setValue(0)
        QtWidgets.QApplication.processEvents()

        # A videoProcessor object is created and the frameGrabber function inside
        # of it will grab every single frame of a video and append its RGB values to an array
        self.processor = VideoProcessor(self.videoPath)

        grabbingProgress = self.processor.frameGrabber()

        for value in grabbingProgress:
            self.progressBar.setValue(int(value))
            QtWidgets.QApplication.processEvents()

        text = "Done grabbing frames"
        self.progressLabel.setText(text)
        self.progressBar.setValue(20)
        QtWidgets.QApplication.processEvents()

        time.sleep(2)

        text = "Processing frames..."
        self.progressLabel.setText(text)
        QtWidgets.QApplication.processEvents()

        processProgress = self.processor.frameProcessor()

        for value in processProgress:
            self.progressBar.setValue(int(value))
            QtWidgets.QApplication.processEvents()


        self.progressBar.setValue(100)

        text = "Done processing the " + str(len(self.processor.grabbedFrames)) + \
        " frames of " + self.selectedVideo.text()
        self.progressLabel.setText(text)

#******************************************************************************
    """
    This function updates the video input path
    """

    def videoPathChanged(self):

        self.selectedVideo = self.videoList.currentItem()

        # Makes the file/folder names readable by making spaces readable
        self.videoDirectory = self.videoDirectory.replace(' ', '\ ')

        self.videoPath = self.videoDirectory + "/" + self.selectedVideo.text()

        self.player.videoPath = self.videoPath

        self.player.openFile()

#******************************************************************************

    """
    This function updates the values of the stimulusProtocol inside of the controller
    """
    def updateController(self):

        self.deviceController = DeviceController(self.graph.x, self.graph.y, \
                                                self.conditions, self.graph.runningTime, \
                                                self.notRandomRadioButton.isChecked())


#******************************************************************************
