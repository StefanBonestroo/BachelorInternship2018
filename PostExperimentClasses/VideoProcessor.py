
"""
VideoProcessor.py

This class handles the processing of videos to analyze. It contains functions for
grabbing frames and for processing those frames using different techniques.

created by: Stefan Bonestroo
date created: 20/02/2018
date last modified: 12/02/2018

"""

import cv2
import time
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets

class VideoProcessor:

    def __init__(self, path, preview, startFrame):

        self.path = path

        self.terminated = False

        self.processedFrames = None

        self.referenceFrame = None
        self.lastDifferenceFrame = None
        self.numberOfFrames = 0
        self.AllROI = []
        self.preview = preview

        # This opens a video capture
        self.capture = cv2.VideoCapture(self.path)

        self.numberOfFrames = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.capture.get(cv2.CAP_PROP_FPS))
        self.increment = 100/self.numberOfFrames

        if preview:

            self.capture.set(1, startFrame - 1)

#*******************************************************************************

    def frameGrabber(self):

        """
        This function grabs every single frame of a video at a certain path, and
        stores these in an array.
        """

        if not self.capture.isOpened():
            return

        if self.numberOfFrames == 0:
            return None

        while (self.capture.isOpened()):

            succesful, frame = self.capture.read()

            if succesful:

                yield frame

            if self.terminated:
                return


#*******************************************************************************

    def frameProcessor(self, frame, gaussianBlur, useBlank, pixelThreshold, dilation, averageDifferenceFrames):

        """
        This function processes the grabbed frames in 'self.grabbedFrames' using
        different techniques.
        """

        # A frame will converted to a grayscale image
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Makes sure the first screen is black
        if self.referenceFrame is None:
            self.referenceFrame = grayImage

        # Max a black and white view of the absolute difference between the
        # image and the reference frame
        difference = cv2.absdiff(self.referenceFrame, grayImage)

        # If a user has chosen the option of 'averaging between difference frames'
        if averageDifferenceFrames:

            if self.lastDifferenceFrame is None:
                self.lastDifferenceFrame = difference

            # The average is half the value of every pixel of a difference frame +
            # the other half from the next difference frame (sliding window)
            image = 0.5 * self.lastDifferenceFrame + 0.5 * difference

        else:

            image = difference

        if gaussianBlur[0]:

            # A Gaussian blur will be applied to that frame to cancel out noise
            image = cv2.GaussianBlur(image, (gaussianBlur[1], gaussianBlur[1]), 0)

        # Threshold the data using the data the user has entered
        image = cv2.threshold(image, pixelThreshold, 255, cv2.THRESH_TOZERO)[1]

        # Dilate the thresholded image to fill in holes
        image = cv2.dilate(image, None, iterations = dilation)
        image *= 2

        self.lastDifferenceFrame = difference
        self.referenceFrame = grayImage

        i = 0

        # Every ROI is cut out of the processed frame
        for ROI in self.AllROI:

            r = ROI
            processedFrame = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

            # The preview is showed if desired
            if self.preview:

                cv2.imshow('Preview', processedFrame)
                cv2.waitKey(1)
                time.sleep(1/self.fps)

            else:

                # x is the timestamp/frametime
                timestamp = len(self.processedFrames[i][1]) * (1/self.fps)
                self.processedFrames[i][0].append(round(timestamp,4))

                # y is the amount of white pixels in the processed frame
                self.processedFrames[i][1].append(np.sum(processedFrame > 0))

            i += 1

        return
