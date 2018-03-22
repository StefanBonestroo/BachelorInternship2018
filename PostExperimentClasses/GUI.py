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

class GUI(QtWidgets.QMainWindow, GUIFiles.postExperimentGUI.Ui_MainWindow):

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

        self.runAnalysisButton.clicked.connect(self.runAnalysis)
        self.processor = None

#******************************************************************************

        # This is where the selected video path is stored
        self.videoPath = None

        self.videoList.currentItemChanged.connect(self.videoPathChanged)
        self.videoWidget.mediaPlayer.error.connect(self.handleError)

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

    def runAnalysis(self):

        """
        This function runs the analysis of the selected video material when 'Run Analysis'
        is pressed.
        """

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
