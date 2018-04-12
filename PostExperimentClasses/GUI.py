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

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets


import GUIFiles.postExperimentGUI

from PostExperimentClasses.VideoProcessor import VideoProcessor
from PostExperimentClasses.VideoPlayer import VideoPlayer
from PostExperimentClasses.VideoCutter import VideoCutter

class GUI(QtWidgets.QMainWindow, GUIFiles.postExperimentGUI.Ui_MainWindow):

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

        # Triggers 'setInputDirectory' on the button press
        self.setInputDirectoryButton.clicked.connect(self.setInputDirectory)
        self.videoDirectory = None

#******************************************************************************

        self.runAnalysisButton.clicked.connect(self.runAnalysis)
        self.stopAnalysisButton.clicked.connect(self.stopAnalysis)
        self.processor = None

#******************************************************************************

        # This is where the selected video path is stored
        self.videoPath = None

        self.videoList.currentItemChanged.connect(self.videoPathChanged)
        self.videoWidget.mediaPlayer.error.connect(self.handleError)

#******************************************************************************

        self.cutter = None

        self.selectRoiButton.clicked.connect(self.selectROI)
        self.clearRoiButton.clicked.connect(self.clearROI)

#******************************************************************************

    def setInputDirectory(self):

        """
        This function lets the user pick a directory and will present all relevant
        files inside a QListWidget (video files in our case).
        """

        # The list is cleared
        self.videoList.clear()

        # A directory picker is opened
        self.videoDirectory = QtWidgets.QFileDialog.getExistingDirectory(self,"Choose your directory")

        # If a directory has been chosen, iterate over all files en add all videofiles to the list
        if self.videoDirectory:

            for video in os.listdir(self.videoDirectory):

                if video.endswith(".mov") or video.endswith(".mp4") or video.endswith(".MP4"):

                    self.videoList.addItem(video)

#******************************************************************************

    def selectROI(self):

        if self.videoPath != None:

            image, height, width = self.videoWidget.getPreview()

            self.cutter = VideoCutter(image)

            ROI = self.cutter.selectROI()

            self.roiListWidget.addItem(str(ROI))

#******************************************************************************

    def clearROI(self):

        self.roiListWidget.clear()

#******************************************************************************

    def runAnalysis(self):

        """
        This function runs the analysis of the selected video material when 'Run Analysis'
        is pressed.
        """

        self.runAnalysisButton.setEnabled(False)

        self.progressLabel.setText("Grabbing frames...")
        self.progressBar.setValue(0)
        QtWidgets.QApplication.processEvents()

        if self.roiListWidget.item(0) == None:

            self.progressLabel.setText("Provide at least one Region Of Interest (ROI).")
            QtWidgets.QApplication.processEvents()
            return

        # A videoProcessor object is created and the frameGrabber function inside
        self.processor = VideoProcessor(self.videoPath)
        grabber = self.processor.frameGrabber()

        for i in range(self.roiListWidget.count()):

            ROI = self.roiListWidget.item(i).text()
            ROI = list(eval(ROI))
            self.processor.AllROI.append(ROI)

        self.processor.processedFrames = [[] for _ in range(self.roiListWidget.count())]
        self.processor.referenceFrame = None
        counter = 0
        value = 0

        for grabbedFrame in grabber:

            text = "Processing frame " + str(counter) + " of " + str(self.processor.numberOfFrames) + " frames..."
            self.progressLabel.setText(text)
            QtWidgets.QApplication.processEvents()

            self.processor.frameProcessor(grabbedFrame)

            if self.processor.terminated:

                self.progressLabel.setText("The analysis was stopped.")
                self.progressBar.setValue(0)
                QtWidgets.QApplication.processEvents()
                break

            counter += 1

            value += self.processor.increment
            self.progressBar.setValue(value)
            QtWidgets.QApplication.processEvents()

        if not self.processor.terminated:

            self.progressBar.setValue(100)
            text = "Done processing the " + str(self.processor.numberOfFrames) + \
            " frames of " + self.selectedVideo.text()
            self.progressLabel.setText(text)

        self.runAnalysisButton.setEnabled(True)

#******************************************************************************

    def stopAnalysis(self):

        self.processor.terminated = True

#******************************************************************************


    def videoPathChanged(self):

        """
        This function updates the video input path
        """

        self.selectedVideo = self.videoList.currentItem()

        # Makes the file/folder names readable by making spaces readable
        self.videoDirectory = self.videoDirectory.replace(' ', '\ ')

        self.videoPath = self.videoDirectory + "/" + self.selectedVideo.text()

        self.videoWidget.videoPath = self.videoPath
        self.videoWidget.openFile()

#******************************************************************************

    def handleError(self):

        # The media player will return an error string if something went wrong
        self.progressLabel.setText("Error: " + self.videoWidget.mediaPlayer.errorString())
