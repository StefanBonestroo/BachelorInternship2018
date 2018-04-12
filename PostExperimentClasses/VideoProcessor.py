
"""
VideoProcessor.py

This class handles the processing of videos to analyze. It contains functions for
grabbing frames and for processing those frames using different techniques.

created by: Stefan Bonestroo
date created: 20/02/2018
date last modified: 12/02/2018

"""

import cv2

from PyQt5 import QtCore, QtGui, QtWidgets

class VideoProcessor:

    def __init__(self, path):

        self.path = path

        self.terminated = False

        self.processedFrames = [[]]

        self.fps = 120
        self.referenceFrame = None
        self.numberOfFrames = 0
        self.AllROI = []

#*******************************************************************************

    def frameGrabber(self):

        """
        This function grabs every single frame of a video at a certain path, and
        stores these in an array.
        """

        # This opens a video capture
        capture = cv2.VideoCapture(self.path)

        if not capture.isOpened():
            print("Error opening video file")
            return

        self.numberOfFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.increment = 100/self.numberOfFrames

        # Stores the RGB values of every single frame in 'grabbedFrames'
        while (capture.isOpened()):

            succesful, frame = capture.read()

            if succesful:

                yield frame

            if self.terminated:
                return


#*******************************************************************************

    def frameProcessor(self, frame):

        """
        This function processes the grabbed frames in 'self.grabbedFrames' using
        different techniques.
        """

        # A frame will converted to a grayscale image
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # A Gaussian blur will be applied to that frame to cancel out noise
        blurredImage = cv2.GaussianBlur(grayImage, (21, 21), 0)

        # Makes sure the first screen is black
        if self.referenceFrame is None:
            self.referenceFrame = blurredImage

        # Max a black and white view of the absolute difference between the
        # image and the reference frame
        frameDelta = cv2.absdiff(self.referenceFrame, blurredImage)
        threshold = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # Dilate the thresholded image to fill in holes
        threshold = cv2.dilate(threshold, None, iterations=2)

        self.referenceFrame = blurredImage

        for ROI in self.AllROI:
            r = ROI
            processedFrame = threshold[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

        return
