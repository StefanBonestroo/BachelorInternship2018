"""
GUI.py

The class in this file describes the Graphical User Interface (GUI) with all the possible
interactions a user can have with it.

created by: Stefan Bonestroo
date created: 08/02/2018
date last modified: 12/03/2018
"""

import os
import sys
import random
import time
import threading
import numpy as np

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from goprocam import constants
from PyDAQmx import *

import GUIFiles.preExperimentGUI
from PreExperimentClasses.StimulusPlot import StimulusPlotCanvas
from PreExperimentClasses.Controller import DeviceController
from PreExperimentClasses.GoProConnector import GoPro

class GUI(QtWidgets.QMainWindow, GUIFiles.preExperimentGUI.Ui_MainWindow):

    def __init__(self, parent = None):

        # This tells GUI to inherit everything initiated by the design.py file
        # which contains all information about the front-end of the GUI
        super(GUI, self).__init__(parent)
        self.setupUi(self)

        screen = self.frameGeometry()
        centre = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(centre)
        self.move(screen.topLeft())

#******************************************************************************

        self.outputDirectory = None
        self.currentFile = None

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

        self.downloadLastDataButton.clicked.connect(self.downloadData)

#******************************************************************************

        self.setOutputDirectoryButton.clicked.connect(self.setOutputDirectory)

#******************************************************************************

        # Timer for the little stimulus bleep
        self.bleepTimer = QtCore.QTimer()
        self.bleepTimer.timeout.connect(self.graph.bleepShower)

#******************************************************************************

        self.runButton.clicked.connect(self.runExperiment)
        self.resetButton.clicked.connect(self.terminateExperiment)

        self.deviceController = None
        self.updateController()

        self.setCleanChannel.clicked.connect(self.updateController)

#******************************************************************************

        self.camera = None
        self.connectCameraButton.clicked.connect(self.connectCamera)

#******************************************************************************

    def updateStimulusPlot(self):

        """
        This function will use the info from the spinboxes to construct
        a stimulus plot to be viewed inside of the canvas.
        """

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

    def addToProtocol(self):

        """
        This function populates the stimulus protocol list with conditions entered by
        the user. A condition is a condition name and a output channel number.
        """

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

    def clearProtocol(self):

        """
        This function clears the stimulus protocol list.
        """

        self.stimulusProtocolList.clear()

        self.channelsTaken = []
        self.conditions = []

        self.graph.conditionLabels = []
        self.updateStimulusPlot()

#******************************************************************************

    def setOutputDirectory(self):

        """
        This function changes the path where the output will be saved in.
        """

        # A directory picker is opened
        self.outputDirectory = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose your directory")

        self.outputDirectoryText.setText(self.outputDirectory)

        # When the experiment data output directory is selected, the path will be
        # set to this location
        if self.currentFile != None:
            self.currentFile.close()

        try:
            self.currentFile = open(self.outputDirectory + "/experimentData.txt", "a+")
        except:
            self.runtimeErrorLabel.setText("Please, pick a directory.")


#******************************************************************************

    def downloadData(self):

        """
        This function downloads the most recently shot media.
        """

        if self.currentFile == None:

            self.runtimeErrorLabel.setText("No directory was selected.")
            return

        elif self.camera == None:

            self.runtimeErrorLabel.setText("Not connected to a GoPro.")
            return

        self.runtimeErrorLabel.setText("Downloading...")
        time.sleep(0.1)

        # This is stored in the folder where 'main.py' is
        self.camera.cam.downloadLastMedia()

        # The most recent shot video's name is obtained
        name = self.camera.cam.getMedia()
        self.writeExperimentData(name[-12:-4])

        # Only then the next run can be done, since the experiment data will be overwritten
        self.runButton.setEnabled(True)
        self.runtimeErrorLabel.setText("Download succesful!")

#******************************************************************************

    def connectCamera(self):

        """
        This function initiates the camera, and will directly attempt to connect
        with it over wifi.
        """

        self.runtimeErrorLabel.setText("Pairing...")
        time.sleep(0.1)
        self.camera = GoPro()

        # This makes the camera do 'beep'
        self.camera.cam.locate(constants.start)

        self.runButton.setEnabled(True)
        self.runtimeErrorLabel.setText("Pairing succesful!")

        # This makes the camera stop doing 'beep'
        self.camera.cam.locate(constants.stop)

#******************************************************************************

    def runExperiment(self):

        """
        This function will run 'plotStimulus' under different conditions, since the
        stimulusplot is already constructed. This merely controls the little bleep.
        """

        # Only if the conditions have all been given a name, the experiment can be run
        if len(self.conditions) != self.numberSpinBox.value():

            self.runtimeErrorLabel.setText("Error: Not enough conditions.")
            return

        # A output directory should be selected
        elif self.currentFile == None:

            self.runtimeErrorLabel.setText("Error: No directory selected.")
            return

        # If the camera-thread has ended, make a new one.
        else:

            if not self.camera.is_alive():
                self.camera = GoPro()

            self.runtimeErrorLabel.setText("")

        self.updateController()

        # The last value of the x list will be the total running time
        runningTime = self.graph.x[len(self.graph.x) - 1]

        self.graph.runningTime = runningTime
        self.camera.runningTime = runningTime

        self.camera.start()

        # This is the delay between sending the signal and the Go Pro actually recording
        time.sleep(1.3)

        # The connection that this timer has will be executed every 'bleepInterval'
        # milliseconds. This means that 'bleepShower' is triggered every 'bleepInterval' ms
        self.bleepTimer.start(self.graph.bleepInterval)

        time.sleep(0.2)

        # This initiates the deviceController thread, so visualizations and the
        # stimulus protocol can be run at the same time
        self.deviceController.start()

        self.runButton.setEnabled(False)
        self.runtimeErrorLabel.setText("Please, download/save your experiment data.")


#******************************************************************************

    def terminateExperiment(self):

        """
        This function will terminate an experiment run.
        """

        self.bleepTimer.stop()

        self.graph.resetStuff()
        self.updateStimulusPlot()

        self.runButton.setEnabled(True)
        self.runtimeErrorLabel.setText("")

#******************************************************************************

    def updateController(self):

        """
        This function updates the values of the stimulusProtocol inside of the controller
        """

        # Update all values in the deviceController
        self.deviceController = DeviceController(self.graph.x, self.graph.y, \
                                                self.conditions, self.graph.runningTime, \
                                                self.notRandomRadioButton.isChecked())

        # The user selected clean channel
        cleanChannel = self.deviceController.channels[self.cleanChannelSpinBox.value()]
        cleanChannel = np.array(cleanChannel, dtype = np.uint8)

        self.deviceController.allOff = cleanChannel

        # Change the clean channel
        task = Task()
        task.CreateDOChan("/cDAQ1Mod1/port0/line0:7","",DAQmx_Val_ChanForAllLines)

        task.WriteDigitalLines(1, 1, 10.0, DAQmx_Val_GroupByChannel, cleanChannel, None, None)
        task.StopTask()

#******************************************************************************

    def writeExperimentData(self, videoFileName):

        """
        This function writes to a .txt file, the information concerning the previously
        run experiment.
        """

        if self.currentFile.closed:

            self.currentFile = open(self.outputDirectory + "/experimentData.txt", "a+")

        self.currentFile.write("--------------------------------------------------\n")
        self.currentFile.write("EXPERIMENT DATA - RUN: " + time.asctime() + "\n")
        self.currentFile.write("--------------------------------------------------\n\n")

        self.currentFile.write("Conditions: " + str(self.conditions) + "\n")
        self.currentFile.write("Random: " + str((not True)) + "\n")

        self.currentFile.write("GoPro filename: " + videoFileName +"\n")
        self.currentFile.write("Notes: " + self.notesText.toPlainText() + "\n")

        self.currentFile.write("Copied data into lab journal: NO\n\n\n")

        self.currentFile.close()
