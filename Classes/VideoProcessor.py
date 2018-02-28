
"""
VideoProcessor.py

This class handles the processing of videos to analyze. It contains functions for
grabbing frames and for processing those frames using different techniques.

created by: Stefan Bonestroo
date created: 20/02/2018
date last modified: 21/02/2018

"""

import cv2
import time
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets

class VideoProcessor:

    def __init__(self, path):

        self.path = path

        self.grabbedFrames = []
        self.grabbedPreviewFrames = []

        self.processedFrames = []
        self.processedPreviewFrames = []

        self.dimensions = None

        self.previewDimensions = (500, 281)

        self.fps = 30

#*******************************************************************************

    """
    This function grabs every single frame of a video at a certain path, and
    stores these in an array.
    """
    def frameGrabber(self):

        # This opens a video capture
        capture = cv2.VideoCapture(self.path)

        if not capture.isOpened():
            print("Error opening video file")

        # Stores the RGB values of every single frame in 'grabbedFrames'
        while (capture.isOpened()):

            succesful, frame = capture.read()

            if succesful:

                self.grabbedFrames.append(frame)

                # The unprocessed are made to also have preview versions
                preview = cv2.resize(frame, self.previewDimensions)
                preview = bytearray(preview)
                preview = QtCore.QByteArray(preview)

                self.grabbedPreviewFrames.append(preview)

            else:
                break

        # When everything done, release the video capture object
        capture.release()

        self.frameProcessor()

#*******************************************************************************

    """
    This function processes the grabbed frames in 'self.grabbedFrames' using
    different techniques.
    """
    def frameProcessor(self):

        # The reference frame will be the previous frame
        referenceFrame = None

        for frame in self.grabbedFrames:

            # A frame will converted to a grayscale image
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # A Gaussian blur will be applied to that frame to cancel out noise
            blurredImage = cv2.GaussianBlur(grayImage, (21, 21), 0)

            # Makes sure the first screen is black
            if referenceFrame is None:
                referenceFrame = blurredImage

            # Max a black and white view of the absolute difference between the
            # image and the reference frame
            frameDelta = cv2.absdiff(referenceFrame, blurredImage)
            threshold = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

            # Dilate the thresholded image to fill in holes
            threshold = cv2.dilate(threshold, None, iterations=2)
            # writableFrame = cv2.cvtColor(threshold,cv2.COLOR_GRAY2BGR)

            referenceFrame = blurredImage

            # The processed frame will be stored in an array
            self.processedFrames.append(threshold)

            # A preview of the processed frame is made
            preview = cv2.resize(threshold, self.previewDimensions)
            preview = bytearray(preview)
            preview = QtCore.QByteArray(preview)

            self.processedPreviewFrames.append(preview)

        self.dimensions = threshold.shape
