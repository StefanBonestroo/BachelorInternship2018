"""
GUI.py

The class in this file describes the Graphical User Interface (GUI) with all the possible
interactions a user can have with it.

created by: Stefan Bonestroo
date created: 08/02/2018
date last modified: 13/02/2018
"""

import os
import sys

import random
import design
from PyQt5 import QtCore, QtGui, QtWidgets

from Classes.StimulusPlot import StimulusPlotCanvas

class GUI(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent = None):

        # This tells GUI to inherit everything initiated by the design.py file
        # which contains all information about the front-end of the GUI
        super(GUI, self).__init__(parent)
        self.setupUi(self)

#******************************************************************************

        # Triggers 'setDirectory' on the button press
        self.setDirectoryButton.clicked.connect(self.setDirectory)

#******************************************************************************

        # A box is placed that will hold the canvas for the stimulus plot, and
        # the canvas is initiated.
        self.box = QtWidgets.QVBoxLayout(self.stimulusPlot)
        self.graph = StimulusPlotCanvas(self.stimulusPlot, width = 5, height = 4, dpi = 100)
        self.box.addWidget(self.graph)

#******************************************************************************

        # When the values of the stimulus program change, 'updateStimulusPlot'
        # will trigger
        self.preSpinBox.valueChanged.connect(self.updateStimulusPlot)
        self.stimSpinBox.valueChanged.connect(self.updateStimulusPlot)
        self.interSpinBox.valueChanged.connect(self.updateStimulusPlot)
        self.numberSpinBox.valueChanged.connect(self.updateStimulusPlot)

#******************************************************************************

        # Triggers 'showExperiment' on the button press
        self.runButton.clicked.connect(self.showExperiment)

#******************************************************************************

    """
    This function lets the user pick a directory and will present all relevant
    files inside a QListWidget (video files in our case).
    """
    def setDirectory(self):

        # The list is cleared
        self.videoList.clear()

        # A directory picker is opened
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose your directory")

        # If a directory has been chosen, iterate over all files en add all videofiles to the list
        if directory:

            for video in os.listdir(directory):

                if video.endswith(".mov") or video.endswith(".avi"):

                    self.videoList.addItem(video)

#******************************************************************************

    """
    This function will use the info from the spinboxes to construct
    a stimulus plot to be viewed inside of the canvas.
    """
    def updateStimulusPlot(self, running):

        # The spinbox values are obtained
        pre = self.preSpinBox.value()
        stimulus = self.stimSpinBox.value()
        interval = self.interSpinBox.value()
        repeats = self.numberSpinBox.value()


        x = [0]
        y = [0]

        # The course of the stimulus plot will be put into a list, so we can plot from it
        x.append(pre)
        y.append(1)

        time = pre

        # Since a stimulus can be presented multiple times, the same combo of
        # stimulus + interval will be pasted n ('repeats') times
        for repeat in range(repeats):

            time += stimulus
            x.append(time)
            y.append(0)

            time += interval
            x.append(time)
            y.append(1)

        # The last value of y should be 0, so that the plot looks nice
        y[len(y) - 1] = 0

        # Also a 'nice-maker
        if stimulus == 0:
            y = [0] * len(y)

        # Tells the canvas what the values of x and y are
        self.graph.x = x
        self.graph.y = y

        # Tells the canvas to plot the stimulus and present it
        self.graph.plotStimulus()
        self.graph.draw()

#******************************************************************************

    """
    This function will run 'plotStimulus' under different conditions, since the
    stimulusplot is already constructed. This merely controls the little bleep.
    """
    def showExperiment(self):

        self.graph.running = True
        self.graph.plotStimulus()
