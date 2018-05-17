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
from PostExperimentClasses.DataPlotter import plotRawData, makeSpectrogram, plotPowerSpectrum

from PostExperimentClasses.OutputSaver import OutputSaver


class GUI(QtWidgets.QMainWindow, GUIFiles.postExperimentGUI.Ui_Analysis):

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

        self.previewOutputButton.clicked.connect(self.runPreview)

#******************************************************************************

        self.visualizeDataButton.clicked.connect(self.visualizeData)
        self.saveRawDataButton.clicked.connect(self.saveRawData)
        self.saveOutputButton.clicked.connect(self.openSaveScreen)

        self.outputSaver = OutputSaver()

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

        """
        The function allows the user to select Regions of Interest (ROI).
        """

        if self.videoPath != None:

            # image, height, width = self.videoWidget.getPreview()

            # self.cutter = VideoCutter(image)

            # ROI = self.cutter.selectROI()

            self.roiListWidget.addItem("(314, 56, 390, 348)")
            self.roiListWidget.addItem("(700, 53, 396, 340)")
            self.roiListWidget.addItem("(272, 452, 451, 413)")


#******************************************************************************

    def clearROI(self):

        self.roiListWidget.clear()

#******************************************************************************

    def runPreview(self):

        """
        This function runs a 5 second preview of the processed frames.
        """

        self.runAnalysis(True)

        self.progressBar.setValue(0)
        QtWidgets.QApplication.processEvents()

#******************************************************************************

    def runAnalysis(self, preview = False):

        """
        This function runs the analysis of the selected video material when 'Run Analysis'
        is pressed.
        """

        self.runAnalysisButton.setEnabled(False)

        # User options are stored in these variables
        gaussianBlur = []
        gaussianBlur.append(self.gaussianCheckBox.isChecked())
        gaussianBlur.append(self.gaussianSpinBox.value())

        averageDifferenceFrames = self.middleFrameCheckBox.isChecked()
        useBlank = self.useBlankCheckBox.isChecked()
        pixelThreshold = self.thresholdSpinBox.value()
        dilation = self.dilationSpinBox.value()
        startFrame = self.frameNumberSpinBox.value()

        self.progressLabel.setText("Grabbing frames...")
        self.progressBar.setValue(0)
        QtWidgets.QApplication.processEvents()


        # The user must enter at least one ROI
        if self.roiListWidget.item(0) == None:

            self.progressLabel.setText("Provide at least one Region Of Interest (ROI).")
            self.runAnalysisButton.setEnabled(True)
            QtWidgets.QApplication.processEvents()
            return

        # A videoProcessor object is created and the frameGrabber function inside
        self.processor = VideoProcessor(self.videoPath, preview, startFrame)
        grabber = self.processor.frameGrabber()


        # If the user selected the preview option preview only the selected ROI
        if preview:

            item = self.roiListWidget.currentItem()
            if item == None:

                self.progressLabel.setText("Select a Region Of Interest (ROI).")
                QtWidgets.QApplication.processEvents()
                return True

            ROI = item.text()
            ROI = list(eval(ROI))
            self.processor.AllROI.append(ROI)

            self.processor.increment = 100/(5 * self.processor.fps)

        # Else fully process all the frames for all ROIs
        else:

            for i in range(self.roiListWidget.count()):

                ROI = self.roiListWidget.item(i).text()
                ROI = list(eval(ROI))
                self.processor.AllROI.append(ROI)

        # This creates the data structure where all data will be stored:
        # A list containing lists for every ROI, which then contain an x and a y value
        self.processor.processedFrames = [[list() for i in range(2)] for j in range(self.roiListWidget.count())]
        self.processor.referenceFrame = None

        # Frame counter
        counter = 1
        # Value of the progress bar
        value = 0

        # For every frame yielded from the frame grabber do this:
        for grabbedFrame in grabber:

            if preview:
                text = "Showing 5-second preview..."
            else:
                text = "Processing frame " + str(counter) + " of " + \
                        str(self.processor.numberOfFrames) + " frames..."

            self.progressLabel.setText(text)
            QtWidgets.QApplication.processEvents()

            # Give the frame + a bunch of options to the processor
            self.processor.frameProcessor(grabbedFrame, gaussianBlur, useBlank,\
                                            pixelThreshold, dilation,\
                                            averageDifferenceFrames)

            # The user can stop the analysis, thats when this runs
            if self.processor.terminated:

                self.progressLabel.setText("The analysis was stopped.")
                self.progressBar.setValue(0)
                QtWidgets.QApplication.processEvents()
                break

            counter += 1

            # Change the progress bar value
            value += self.processor.increment
            self.progressBar.setValue(value)
            QtWidgets.QApplication.processEvents()

            # If all frames have been processed end
            if counter >= self.processor.numberOfFrames:
                break
            # For the preview, it is after 5 seconds
            elif counter >= (5 * self.processor.fps) and preview:
                break

        # If a grabber video contains no frames, something went wrong
        if self.processor.numberOfFrames == 0:

            self.progressLabel.setText("Error: Could not open video file")
            self.stopAnalysis()
            self.progressBar.setValue(0)

        # If everything goes well, communicate it to the user.
        if not self.processor.terminated and not preview:

            self.progressBar.setValue(100)
            text = "Done processing the " + str(self.processor.numberOfFrames) + \
            " frames of " + self.selectedVideo.text()
            self.progressLabel.setText(text)
            data = self.processor.processedFrames

            makeSpectrogram(data,self.processor.fps)

        elif preview:

            self.progressLabel.setText("")

        # Release stuff
        self.processor.capture.release()
        cv2.destroyAllWindows()

        self.runAnalysisButton.setEnabled(True)
        QtWidgets.QApplication.processEvents()

#******************************************************************************

    def stopAnalysis(self):

        """
        This function terminates the experiment
        """

        if self.processor != None:
            self.processor.terminated = True

        self.runAnalysisButton.setEnabled(True)

#******************************************************************************


    def videoPathChanged(self):

        """
        This function updates the video input path
        """

        self.progressLabel.setText("")
        self.progressBar.setValue(0)

        self.selectedVideo = self.videoList.currentItem()

        # Makes the file/folder names readable by making spaces readable
        self.videoDirectory = self.videoDirectory.replace(' ', '\ ')

        if self.selectedVideo == None:
            return

        self.videoPath = self.videoDirectory + "/" + self.selectedVideo.text()

        self.videoWidget.videoPath = self.videoPath
        self.videoWidget.openFile()

#******************************************************************************

    def handleError(self):

        # The media player will return an error string if something went wrong
        self.progressLabel.setText("Error: " + self.videoWidget.mediaPlayer.errorString())

#******************************************************************************

    def visualizeData(self):

        data = self.processor.processedFrames
        samplingRate = self.processor.fps

        if self.rawDataCheckBox.isChecked():

            plotRawData(data)

        if self.spectrogramCheckBox.isChecked() or self.powerSpectrumCheckBox.isChecked():

            makeSpectrogram(data, samplingRate)



#******************************************************************************

    def openSaveScreen(self):

        self.outputSaver.show()

#******************************************************************************

    def saveRawData(self):

        name, useless = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "data")

        data = self.processor.processedFrames

        counter = 1

        for chamber in data:

            path = name + str(counter) + ".csv"

            file = open(path, "w")

            headers = "time (s); totalPixelValue\n"
            file.write(headers)

            for datapoint in range(0,len(chamber[0])):

                x = chamber[0][datapoint]
                y = chamber[1][datapoint]
                print(str(x))

                row = str(x) + ";" + str(y) + "\n"
                file.write(row)

            counter += 1
            file.close()
